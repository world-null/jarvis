import os
import re
from playsound import playsound
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
# playing assistance sound function
@eel.expose
def playassistantsound():
    music_dir="www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

def opencommand(query):
    query=query.replace(ASSISTANT_NAME, "")
    query=query.replace("open", "")
    query.lower()

    if query !="":
        speak("opening" + query)
        os.system('start '+ query)
    else:
        speak("not found")

def playyoutube(query):
    searchTerm= extract_yt_term(query)
    speak("playing "+searchTerm+" on youtube")
    kit.playonyt(searchTerm)

def extract_yt_term(command):
    # define a regular expression pattern to capture the song name
    pattern= r'play\s+(.*?)\s+on\s+youtube'
    # use re.search to to find the match in the command
    match=re.search(pattern,command,re.IGNORECASE)
    # if any match is found return the extract song; otherwise return none
    return match.group(1) if match else None 