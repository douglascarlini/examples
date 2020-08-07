
# Author: https://github.com/douglascarlini

# pip install speech-recognition
# pip install pyaudio
# pip install pyttsx3

import speech_recognition as sr
import pyttsx3 as p

ttx = p.init()
mic = sr.Recognizer()

def run():

    with sr.Microphone() as source:

        print('[INFO] adjusting ambient noise...')
        mic.adjust_for_ambient_noise(source)

        print('[INFO] listening...')
        text = mic.listen(source)

        try:

            print('[INFO] recognizing text...')
            said = mic.recognize_google(text)

            print(said)
            ttx.say("OK")
            ttx.runAndWait()

        except sr.UnknownValueError:

            print("unknown value")

        except sr.RequestError as e:

            print("request error")

    run()

run()
