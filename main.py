from time import sleep
from tkinter import *
from tkinter.ttk import Progressbar
from source.builder import buildTemplate


def execute():
    # Fake progress bar lmao
    progress['value'] = 50
    window.update_idletasks()
    buildTemplate(10)
    progress['value'] = 100


window = Tk()
window.wm_geometry("600x500")

l1 = Label(window, text="Δημιουργία React Native GUI!")
l1.grid(row=0)

l2 = Label(window, text="Επιλέξτε τη θέση του μενού!")
l2.grid(row=1)

menu_position = IntVar()
r1 = Radiobutton(window, text="Μενού Επάνω", variable=menu_position, value=1)
r2 = Radiobutton(window, text="Μενού Κάτω", variable=menu_position, value=2)
r3 = Radiobutton(window, text="Χωρίς Μενού", variable=menu_position, value=3)

r1.grid(column=0, row=2)
r2.grid(column=1, row=2)
r3.grid(column=2, row=2)

b1 = Button(window, text="Δημιουργία GUI", command=execute)
b1.grid(row=3)

progress = Progressbar(window, orient=HORIZONTAL, length=200)
progress.grid(row=4)

window.mainloop()
