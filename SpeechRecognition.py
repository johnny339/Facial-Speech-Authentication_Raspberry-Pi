import speech_recognition as sr
import pyttsx3 
import os
from subprocess import Popen

  
# Initialize recognizer 
speechRecognizer = sr.Recognizer() 

# Speak text aloud
def speak(command):
    if command == "start facial authentication":
        # Run facial recognition program
        Popen(["python3", "fr.py"])
    if command == "terminate":
        # Terminate both speech and facial recognition
        Popen(["killall", "python3"])
    
    else :  
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(command) 
        engine.runAndWait()
      
      
# Loop indefinitely   
while True:    
    try:
        # use microphone to hear speech
        with sr.Microphone() as source:
            speechRecognizer.energy_threshold = 2000
            
            # adjusts threshold for ambient noise 
            # speechRecognizer.adjust_for_ambient_noise(source, duration=0.2)
              
            # listens for the user's input 
            speech = speechRecognizer.listen(source)
              
            # Google Web Speech API
            speech_toText = speechRecognizer.recognize_google(speech)
            speech_toText = speech_toText.lower()
  
            print("You said \"" + str(speech_toText) + "\"")
            speak(speech_toText)

    except sr.UnknownValueError:
        print("unknown error occured")

