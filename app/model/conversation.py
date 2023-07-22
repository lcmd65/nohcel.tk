
class Conversation():
    def __init__(self, text):
        self._text = []
        self.add(text)
    
    def add(self, text):
        self._text.append(text)
    
    def get(self, index):
        return self._text[index]


        
    