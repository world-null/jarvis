import os
import eel

from engine.features import *
from engine.command import *

eel.init("www")
playassistantsound()

os.system('start chrome.exe --app="http://localhost:8000/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)
