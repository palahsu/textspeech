import tkinter as tk
from tkinter import *
from gtts import gTTS
import os
    
def toAudio():
        
       text = entry.get()  
       language='en'
       myvoice=gTTS(text,lang=language,slow=False)
       myvoice.save('audioout.mp3')
       os.system("audioout.mp3")
#Window
window = tk.Tk()
window.title("Text To Speech")
window.geometry("400x200")

#InputSpace
entry = StringVar()
point = Entry(
    window,
    font = ("Roboto", 16),
    textvariable = entry,
)
point.grid(pady=50, padx=65, ipady=5, ipadx=5)


#Button
button = tk.Button(window, text="OK", command=toAudio)
button.grid(ipady=5,ipadx=25)
            
            
window.mainloop()
