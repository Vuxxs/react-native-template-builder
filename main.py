from time import sleep
from tkinter import *
from tkinter.ttk import Progressbar
from source.builder import buildTemplate


def execute():
    # Fake progress bar lmao
    progress['value'] = 50
    window.update_idletasks()
    buildTemplate()
    progress['value'] = 100


window = Tk()
window.wm_geometry("300x200")

Label(window, text="Δημιουργία React Native GUI!").pack()

Button(window, text="Δημιουργία GUI", command=execute).pack()

progress = Progressbar(window, orient=HORIZONTAL, length=200)
progress.pack()

window.mainloop()
