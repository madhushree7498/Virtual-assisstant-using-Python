import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
myName = 'hannah'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()




def wishme():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<=12:
        speak('good morning, Madhu')
    elif hour>12 and hour<16:
        speak('good afternoon,madhu')
    else:
        speak('good evening,Madhu')
    speak(f'I am {myName},how may i help you?')



def hearMe():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
    try:
        print('recognizing....')
        query = r.recognize_google(audio,language='en-in')
        print('you said',query)
    except Exception:
        print('say that again, please')
        return 'none'
    return query

if  __name__  ==  "__main__":
    wishme()
    while True:
        query = hearMe().lower()


        if 'wikipedia' in query:
            speak("searching wikipedia....")
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            print(result)
            speak(result)
        elif 'open google' in query:
            webbrowser.open('www.google.com')
        elif 'open youtube' in query:
            webbrowser.open('www.youtube.com')
        elif 'open my python code' in query:
            os.startfile('C:\\Users\\acer\\AppData\\Local\\Programs\\Python\\Python36')










