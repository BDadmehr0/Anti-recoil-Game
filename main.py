import time
import os

from threading import *
from winsound import Beep
from customtkinter import *

set_appearance_mode("dark")

class Sound:
    def ok():
        Beep(600,200)
    def fail():
        Beep(300,600)
    def warning():
        Beep(200,900)
        
root = CTk()
root.geometry('550x400')
root.title('Css Cheat Crysis')
root.iconbitmap('lannister_115487 (min).ico')

root.mainloop()