# pip install pyaudio

from ast import While
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from playsound import playsound


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello sir !")

    elif hour>=12 and hour<18:
        speak("Hello sir !")   

    else:
        speak("Good evening Pranjal !")  

    speak("i am your assistant sir  Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Say that again please...")
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if _name_ == "_main_":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("sure sir")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("ok sir")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("sure sir")
            webbrowser.open("stackoverflow.com")

        elif 'open instagram' in query:
            speak("sure sir")
            webbrowser.open("instagram.com")

        elif 'vs code' in query:
            speak("sure sir")
            codePath = ("C:\\Users\\pranj\\Downloads\\VSCodeUserSetup-x64-1.84.0.exe")
            os.startfile(codePath)

        elif 'my number' in query:
            speak('''sure sir,your mobile number is 999999999999 ''')
            print(" your number is 9999999999 ")

        elif 'my email id' in query:
            speak('''sure sir,your email id is xyz@gmail.com ''')
            print(" your email id is xyza@gmail.com ")

        elif 'open ai' in query:
            speak("sure sir, Opening openai")
            webbrowser.open("openai.com")   
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f" sure Sir, the time is {strTime}")
        
        elif 'my college' in query:
            speak("sure sir, Opening your college location")
            webbrowser.open("https://www.google.com/maps/place/S.R.M+UNIVERSITY+-K.T.R+Campus/@12.8231483,80.0387914,17z/data=!3m1!4b1!4m6!3m5!1s0x3a52f76d4cecae21:0x4ffbf1222ec00611!8m2!3d12.8231431!4d80.0413663!16s%2Fg%2F11c2jyj5gq?entry=ttu")

        elif 'check mail' in query:
            speak("sure sir, Checking mail")
            webbrowser.open("https://mail.google.com/mail/u/0/#inboxoo")
        
        elif 'december' in query:
            speak(" WE wish you a merry christmas we wish you a merry christmas and a happy new year")
        
        else:
            print("No query matched")