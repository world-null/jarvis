import pyttsx3
import speech_recognition as sr
import eel
import time
def speak(text):
    engin=pyttsx3.init('sapi5')
    voice=engin.getProperty('voices')
    engin.setProperty('voice',voice[1].id)
    engin.setProperty('rate',170)
    eel.DisplayMessage(text)
    #print(voice)
    engin.say(text)
    engin.runAndWait()


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listeing...")
        eel.DisplayMessage("listeing...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source, 10, 6)

    try:
        print("recognizing.....")
        eel.DisplayMessage("recognizing....")
        query= r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
    except Exception as e:
        return ""
    return query.lower()
     
@eel.expose
def allcommand():
    try:
        query=takecommand()
        print(query)
        if "open" in query:
            from engine.features import opencommand
            opencommand(query)

        elif "on youtube" in query:
            from engine.features import playyoutube
            playyoutube(query)
        
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            flag = ""
            contact_no, name = findContact(query)
            if(contact_no != 0):

                if "send message" in query:
                    flag = 'message'
                    speak("what message to send")
                    query = takecommand()
                    
                elif "phone call" in query:
                    flag = 'call'
                else:
                    flag = 'video call'
                    
                whatsApp(contact_no, query, flag, name)

        else:
            print("not found")
    except ImportError as e:
        print("Module Import Error:", e)  # Specific error for import issues
    except AttributeError as e:
        print("Attribute Error:", e)  # In case functions are called incorrectly
    except Exception as e:
        print("Unexpected Error:", e)  # Generic exception handling
    
    eel.ShowHood()