#!/usr/bin/env python
# coding: utf-8

#conda install conda-forge::speechrecognition

import speech_recognition as sr
import pyttsx3
import pywhatkit 

listner=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice=listner.listen(source)
            command=listner.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song=command.replace("play",'')
        talk("playing" + song)
        pywhatkit.playonyt(song)
    else:
        talk("Please say the command again")

run_alexa()
