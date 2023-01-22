import speech_recognition as sr
import pyttsx3
from itertools import cycle

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

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

            if 'feur' or 'coiffeur' in command:
                engine.say("bi")
                engine.runAndWait()

            if 'bi' in command:
                engine.say("naire")
                engine.runAndWait()

            if 'naire' or 'binaire'in command:
                engine.say("veu")
                engine.runAndWait()

            if 'veu' or 'voeux' or 'nerveux' in command:
                engine.say("nir")
                engine.runAndWait()

            if 'nir' or 'venir' in command:
                engine.say("vana")
                engine.runAndWait()

    except:
        pass
    return command

for _ in cycle([True]):
    take_command()
