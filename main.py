import datetime
from time import strftime
import pyttsx3
import speech_recognition as sr
import wikipedia
import os
import random
import webbrowser

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voices',voices[2].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour >12 and hour < 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good evening sir")
    speak("How may I help you!")
    speak("")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        #print(e)
        print("Say it again please....")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            speak(results)
        elif 'play music' in query:
            music_dir = "F:\\Vikas Pandey\\My Music\\alka yagnik"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,10)]))
        
        elif 'the time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'Open google' in query:
            webbrowser.open('https://www.google.co.in/?hl=hi')
