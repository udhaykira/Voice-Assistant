import pyttsx3 as p
import speech_recognition as sr
from selenium_web import inflow
from Utube import music
from news import *
import randfacts 
from jokes import *
from weather import *



engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

speak("Hello sir I am Berlin")
print("Hello sir I am Berlin")
print("Temperature in New Delhi is "+str(temp())+"degree celcius "+ "and with "+str(des()))
speak("Temperature in New Delhi is "+str(temp())+"degree celcius "+ "and with "+str(des()))

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if "what" and "about" and "you" in text:
    print("I am all good sir")
    speak("I am all good sir")
speak("What can i do for you")
print("What can i do for you")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio = r.listen(source)
    text1 = r.recognize_google(audio)
    print(text1)

if "information" in text1 or "about" in text1:
    print("Sure sir, You need information about which topic?")
    speak("Sure sir, You need information about which topic?")
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
        
    speak("Searching {} in wikipedia".format(infor))
    print("Searching {} in wikipedia".format(infor))

    assist = inflow()
    assist.get_info(infor)
    input("Press Enter to close the browser")

elif "play" in text1 or "video" in text1 or "song" in text1:
    print("Which video you want me to play sir?")
    speak("Which video you want me to play sir?")
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening...")
        audio = r.listen(source)
        video = r.recognize_google(audio)
        
    speak("Searching {} in Youtube".format(video))
    print("Searching {} in Youtube".format(video))
    assist = music()
    assist.play(video)
    input("Press Enter to close the Youtube")

elif "news" in text1:
    headlines = news()
    print("Sure sir, Now i will read news for you")
    speak("Sure sir, Now i will read news for you")
    for i in range(len(headlines)):
        print(headlines[i])
        speak(headlines[i])

elif "fact" in text1 or "facts" in text1:
    print("Sure sir")
    x = randfacts.getFact()
    print(x)
    speak("Did you know that, "+x)

elif "jokes" in text1 or "joke" in text1:
    print("Sure sir, get ready for some chuckles")
    ar = joke()
    print(ar[0])
    speak(ar[0])
    print(ar[1])
    speak(ar[1])


