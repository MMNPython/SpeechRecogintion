# -*- coding: utf-8 -*-
"""
Spyder Editor

mmn
"""

import speech_recognition as sr

global x

def speech():
    try:
        with sr.Microphone() as source:
            global x
            r = sr.Recognizer()
            audio = r.listen(source)
            x = r.recognize_google(audio)
    except sr.UnknownValueError:
            print("No idea what you just said, listening again...\n")
            speech()
            
if __name__ == '__main__':
    print('Listening and printing what I heard: \n')
    while True:     
        speech()
        print(x)
        
        #TO DO Add a thing to break out the loop - button press maybe