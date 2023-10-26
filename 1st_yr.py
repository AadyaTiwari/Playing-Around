import datetime
import webbrowser
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import os
import time
import subprocess
import json
import requests
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello, Good Morning!")
        print("Hello, Good Morning!")

    elif hour>=12 and hour<18:
        speak("Hello, Good Afternoon!")
        print("Hello, Good Afternoon!")

    else:
        speak("Hello, good Evening!")
        print("Hello, good Evening!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"

        return statement

print("Loading your personal assistant Nova")
speak("Loading your personal assistant Nova")

wishme()


if __name__=='__main__':
    while True:
        speak("How may I help you?")
        statement = takeCommand().lower()
        if statement == 0:
            continue

        if 'good bye' in statement or 'okay bye' in statement or 'stop' in statement:
            speak("Nova signing out. Good bye")
            print("Nova signing out. Good bye")
            break

        if 'wikipedia' in statement:
            speak('sSearching Wikipedia...')
            statement = statement.replace('wikipedia','')
            results = wikipedia.summary(statement, sentences = 3)
            speak('Acoording to Wikipedia...')
            print(results)
            speak(results)

        elif'open youtube' in statement:
            webbrowser.open_new_tab('https://www.youtube.com')
            speak("youtube is open now")
            time.sleep(5)

        elif 'open spotify' in statement:
            webbrowser.open_new_tab('https://open.spotify.com/')
            speak('spotify is open now')
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab('https://www.google.com')
            speak("Google is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab('https://www.gmail.com')       
            speak("gmail is open now")
            time.sleep(5)

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'search' or 'find' in statement:
            statement = statement.replace('search','')
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'who are you' in statement or 'what can you do' in statement:
            speak("I am Nova, version 1 point 0, your personal assistant. I am programmed to perform mundane tasks such as opening google, gmail, youtube, weather reports, perform searches and a lot more.")

        elif 'who made you' in statement or 'who built you' in statement or 'who created you' in statement:
            speak("My creator is Miss Aadya Tiwari")
            print("My creator is Miss Aadya Tiwari")

        elif "weather" in statement:
            api_key="Apply your unique ID"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

        elif 'log off' in statement or 'sign out' in statement:
            speak("ok, your pc will log off in 10 seconds, make sure you exit form all applications")
            subprocess.call(['shutdown','/1'])

time.sleep(3)
    