import nltk 
import fuzz

class Statement():
    def __init__(self, text):
        self._text = text
        self._token = None
    
    def processingTest(self):
        self._token = nltk.tokenize(self.text)
        for index in range(self._token):
            pass
        """ task here ??"""
        
        return
            
        
        
    


        
    