import pyttsx3
import datetime
import webbrowser as wb
import speech_recognition as sr
import os
friday=pyttsx3.init()
voice=friday.getProperty('voices')
friday.setProperty('voice',voice[0].id)

def speak(audio):
    print("ASSISTANT. "+ audio)
    friday.say(audio)
    friday.runAndWait()
def time():
    time=datetime.datetime.now().strftime("%I : %M : %p ")
    speak(time)
def welcome():
    hour=datetime.datetime.now().hour
    if hour>=6 and hour <= 12:
        speak("Good morning Sir")
    elif hour >=12 and hour<=18:
        speak("Good after noon sir")
    elif hour > 18 and hour <=23:
        speak("Good evening Sir")
    speak("How can I help you ?")

def command():
    c=sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language='en')
        print("Khang "+query)
    except sr.UnknownValueError:
        speak("Please repeat or typing the comment!")
        query=str(input("Your order is : "))
    return query

if __name__=="__main__":
    welcome()
    while True:
        query=command().lower()
        if "google" in query:
            print("What should I search ?")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}" #ep kieu string
            wb.get().open(url)
            speak(f"Here is your {search} on google")
        if "youtube" in query:
            print("What should I search ?")
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}" #ep kieu string
            wb.get().open(url)
            speak(f"Here is your {search} on youtube")
        elif "time" in query:
            time()
        elif "off" in query:
            speak("I'm gonna quit. Good bye")
            quit()

