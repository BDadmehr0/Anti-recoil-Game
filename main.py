from threading import *
from winsound import Beep
from customtkinter import *

class Sound:
    ok = Beep(100,100)
    fail = Beep(200,200)
    warning = Beep(300,300)

