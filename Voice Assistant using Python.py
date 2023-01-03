import pyttsx3 # for the voice pack (pip install pyttsx3)
import datetime# for date and time (inbuilt module i.e you don't have to install it)
import speech_recognition as sr# for giving order (pip install speech)
import pyaudio# important
import wikipedia# to search on wikipediathau. mu message hin karuchi....
import webbrowser# to open web
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #get the voice pack from my pc
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)# to know the time
    if hour>= 0 and hour<12:
        speak("Good morning. This is Jarvis! What can i do for you ?")

    elif hour>=12 and hour<18:
        speak("Good afternoon. This is Jarvis! What can i do for you ?")

    else:
        speak("Good evening. This is Eesha ! What can i do for you ?")

def takeCommand():# It takes michrophone input from the user and returns string output


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        input = (f"I said: {query}\n")
        print(input)
    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("Say that again please")
        return"None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic on exicuting tasks on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("open google")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\mebub\\Desktop\\music'
            music = os.listdir(music_dir)
            print(music)
            os.startfile(os.path.join(music_dir, music[1]))
        elif 'what is the time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%m:%S")
            speak(f"The time is {strTime}")
        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")
        elif 'exit command' in query:
            exit()
        
