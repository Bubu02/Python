import speech_recognition as sr # for giving order (pip install speechrecognition)
import pyautogui # for type any thing (pip install pyautogui)

def takeCommand():# It takes michrophone input from the user and returns string output


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"I said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return"None"
    return query
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()

        if 'send' in query:
            query = query.replace("send"," ")
            pyautogui.typewrite(str(query))
            pyautogui.press("enter")
        elif 'kill terminal' in query:
            exit()
            
        
        
