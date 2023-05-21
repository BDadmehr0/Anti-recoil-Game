import time
import os

from threading import *
from winsound import Beep
from customtkinter import *

class Sound:
    def ok():
        Beep(600,200)
    def fail():
        Beep(300,600)
    def warning():
        Beep(200,900)
        
