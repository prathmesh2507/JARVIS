import os
from playsound import playsound
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME



# Playing System Sound function
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\notification_sounds_1.mp3"
    playsound(music_dir)


def opencommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()
    
    if query != "":
        speak("Opening " + query)
        os.system("start " + query)
    else:
        speak("Please specify the application you want to open.")