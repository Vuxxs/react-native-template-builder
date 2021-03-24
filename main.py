from time import sleep
from tkinter import *
from tkinter.ttk import Progressbar

def panos():
    progress['value'] = 50
    window.update_idletasks()
    sleep(2)
    # Εδώ ο Πάνος κάνει τα μαγικά του
    print('panos')
    progress['value'] = 100


window = Tk()
window.wm_geometry("300x200")

Label(window, text="Δημιουργία React Native GUI!").pack()

Button(window, text="Δημιουργία GUI", command=panos).pack()

progress = Progressbar(window, orient=HORIZONTAL, length=200)
progress.pack()

window.mainloop()
