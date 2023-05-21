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
root.resizable(width=False,height=False)
root.title('Css Cheat Crysis')
root.iconbitmap('lannister_115487 (min).ico')

Title_lb = CTkLabel(root,text='CSS Cheat | Crysis',font=('Roboto',24))
Title_lb.pack(padx=12,pady=10)

opttsions = CTkFrame(root)
opttsions.pack(padx=23,pady=20)


BHOP_btn = CTkButton(opttsions,text='Bhop',font=('bold',15))
BHOP_btn.pack(padx=12,pady=10)

no_rec_btn = CTkButton(opttsions,text='No Recoil',font=('bold',15))
no_rec_btn.pack(padx=12,pady=10)


auto_chat_btn = CTkButton(opttsions,text='Auto Chat',font=('bold',15))
auto_chat_btn.pack(padx=12,pady=10)


root.mainloop()