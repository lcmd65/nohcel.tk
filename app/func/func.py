from functools import partial
import speech_recognition as sr
import pyaudio
from tkinter import messagebox
from app.model.conversation import Statement
from gtts import gTTS
import playsound



def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func

def audioMicroToText():
    """ processing audio from microphone """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = Statement(r.recognize_google(audio,language="vi-VI"))
            text = text.processingTest()
            return text
        except Exception as e:
            messagebox.showerror(title = "Error", message = e)
            
def textToAudio(text):
    """ processing text to audio by google api """
    try:
        output = gTTS(text,lang="vi", slow = False)
        output.save("output.mp3")
        playsound.playsound('output.mp3', True)
    except Exception as e:
        messagebox.showerror(title = "Error", message = e)