from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import pyttsx3
import speech_recognition as sr


# Initialize pyttsx3 engine
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def username():
    speak("Hi i am Nihal,Your personal assistant")
    st.write("What should i call you")
    speak("What should i call you")
    name = getcommand().lower()
    st.write("Welcome Mr",name)
    if name.lower() == "none":
        st.write("Couldn't capture your name. Please try again.")
        return

    speak("Welcome Mister")
    speak(name)
    st.balloons()
    speak("How can i help you")


def getcommand():
    recogniser = sr.Recognizer()

    with sr.Microphone() as source:         
        st.write("Listening...")
        recogniser.pause_threshold = 1
        audio = recogniser.listen(source)
  
    try:
        st.write("Your answer is on the way...")    
        query = recogniser.recognize_google(audio, language ='en-in')
        st.write(f"User said: {query}\n")  
    except Exception as e:
        st.write(e)    
        st.write("Unable to Recognize your voice.")  
        return "None"
     
    return query


