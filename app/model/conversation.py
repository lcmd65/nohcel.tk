import nltk 
import fuzz
import re
import json
from app.func.func import audioToText
class Statement():
    def __init__(self, text):
        self._text = text
        self._token = None
        self._annotations = []
        self._roll = None
    
    def processingAnnotation(self):
        """ annotations processing step 1: embedded database"""
        with open("app/embedded.json") as database:
            data = json.loads(database)
            for item in data:   
                if ("date" in self._annotations) and ("address" in self._annotations):
                    break # decrease complexity
                if self._token.find(item.key()) != None: 
                    if item.get() in self._annotations:
                        pass
                    else:
                        self._annotations.append(item)
                        
    def processingText(self):
        """ processing Acronyms  word"""
        with open("app/embedded_word.json", "r+") as file:
            data = json.loads(file)
        self._token = nltk.tokenize(self.text)
        for index in range(len(self._token)):
            for item in data:
                if self._token[index] == item:
                    self._token[index] = item.get()
                elif index < len(self._token) - 1 and "".join([self._token[index], self._token[index + 1]]) == item:
                    self._token[index] = item.get()
                    self._token.pop(index+1)
        file.close()

    def processingNumberSuffix(self):
        """ processing and normalize number """
        with open("app/embedded_prefix.json", "r+") as prefix:
            data_prefix = json.loads(prefix)
        with open("app/embedded_suffix.json", "r+") as suffix:
            data_suffix = json.loads(suffix)
        for index in range(len(self._token) - 1):
            if self._token[index] in data_prefix.key() and self._token[index + 1] in data_suffix.key():
                self._token[index] = data_prefix[self._token[index]].get() * data_suffix[self._token[index + 1]].get()
                self._token.pop(index + 1) 
        prefix.close()
        suffix.close()
            
    
    def processingNumberContinue(self):
        with open("app/embedded_prefix.json", "r+") as prefix:
            data_prefix = json.loads(prefix)
        for first_index in range(len(self._token)-1):
            if self._token[first_index] in data_prefix.key():
                back = data_prefix[self._token[first_index]].get()
                temp_index = first_index
                for second_index in range(first_index + 1, len(self._token)):
                    if self._token[second_index] in data_prefix.key():
                        back = back*10 + data_prefix[self._token[second_index]].get()
                        temp_index = second_index
                    else:
                        break
                if temp_index > first_index :
                    self._token[first_index] = "".join([self._token[first_index]])
                    self.pop(first_index+ 1, temp_index)
            else:
                pass
    
            
        

class Audio(Statement):
    def __init__(self, audio):
        self._audio = audio
        Statement.__init__(self, audioToText(audio))
    
    
        
    


        
    