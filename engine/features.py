from playsound import playsound
import eel



# Playing System Sound function
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\notification_sounds_1.mp3"
    playsound(music_dir)