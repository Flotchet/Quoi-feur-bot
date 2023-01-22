import speech_recognition as sr
import pyttsx3
from itertools import cycle

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='fr-FR')
            command = command.lower()
            if 'quoi' in command:
                engine.say("feur")
                engine.runAndWait()
    except:
        pass
    return command

for _ in cycle([True]):
    take_command()
