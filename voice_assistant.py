import speech_recognition as sr
from gtts import gTTS
import playsound
import os
from datetime import datetime

def speak(text):
    print("Assistant:", text)
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except:
            return ""

def assistant():
    speak("Hello, I am your voice assistant")

    while True:
        command = listen()

        # Greeting
        if any(word in command for word in ["hello", "hi", "hey"]):
            speak("Hello! How are you?")

        # Name variants
        elif any(word in command for word in [
            "your name", "who are you", "tell me your name", "what should i call you"
        ]):
            speak("My name is Python Voice Assistant")

        # Time variants
        elif any(word in command for word in [
            "time", "current time", "what time is it", "tell me the time"
        ]):
            time = datetime.now().strftime("%H:%M")
            speak("Current time is " + time)

        # Date variants
        elif any(word in command for word in [
            "date", "today date", "what is today's date", "tell me the date"
        ]):
            date = datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + date)

        # Exit variants
        elif any(word in command for word in [
            "exit", "stop", "quit", "close", "bye"
        ]):
            speak("Goodbye!")
            break

        # Default
        else:
            speak("Sorry, I did not understand. Please try again.")

assistant()
