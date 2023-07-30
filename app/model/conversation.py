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
        
    def tranferNumber(prefix, suffix):
        return prefix * suffix
    
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
        with open("app/embedded_label.json", "r+") as file:
            data = json.loads(file)
        self._token = nltk.tokenize(self.text)
        for index in range(len(self._token)):
            for item in data:
                if self._token[index] == item:
                    self._token[index] = item.get()
                elif index < len(self._token) - 1 and "".join([self._token[index], self._token[index + 1]]) == item:
                    self._token[index] = item.get()
                    self._token.pop(index+1)
        

class Audio(Statement):
    def __init__(self, audio):
        self._audio = audio
        Statement.__init__(self, audioToText(audio))
    
    
        
    


        
    