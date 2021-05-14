from tkinter import *
from tkinter.ttk import Progressbar
from source.builder import buildTemplate

def execute():
    entryString = str(num_text_entry.get())
    if entryString.isdigit():
        num_text = int(entryString)
    else:
        num_text = 0
    entryString = str(num_text_input_entry.get())
    if entryString.isdigit():
        num_text_input = int(entryString)
    else:
        num_text_input = 0

    entryString = str(button.get())
    if entryString.isdigit():
        num_button = int(entryString)
    else:
        num_button = 0

    entryString = str(switch.get())
    if entryString.isdigit():
        num_switch = int(entryString)
    else:
        num_switch = 0

    entryString = str(pressable.get())
    if entryString.isdigit():
        num_pressable = int(entryString)
    else:
        num_pressable = 0

    entryString = str(image.get())
    if entryString.isdigit():
        num_image = int(entryString)
    else:
        num_image = 0

    # Fake progress bar lmao
    progress['value'] = 50
    window.update_idletasks()

    buildTemplate(num_text, num_text_input, num_switch, num_pressable, num_image, num_button)

    progress['value'] = 100

window = Tk()
window.wm_geometry("600x500")

row = 0
l1 = Label(window, text="Δημιουργία React Native GUI!")
l1.grid(row=row)
row += 1

ltext = Label(window, text="πόσα πεδία text θέλετε;")
ltext.grid(row=row)
num_text_entry = Entry(window)
num_text_entry.grid(row=row, column=1)
row += 1

ltext = Label(window, text="πόσα πεδία text input θέλετε;")
ltext.grid(row=row)
num_text_input_entry = Entry(window)
num_text_input_entry.grid(row=row, column=1)
row += 1

ltext = Label(window, text="πόσα buttons θέλετε;")
ltext.grid(row=row)
button = Entry(window)
button.grid(row=row, column=1)
row += 1

ltext = Label(window, text="πόσα switches θέλετε;")
ltext.grid(row=row)
switch = Entry(window)
switch.grid(row=row, column=1)
row += 1

ltext = Label(window, text="πόσα images θέλετε;")
ltext.grid(row=row)
image = Entry(window)
image.grid(row=row, column=1)
row += 1

ltext = Label(window, text="πόσα pressables θέλετε;")
ltext.grid(row=row)
pressable = Entry(window)
pressable.grid(row=row, column=1)
row += 1

b1 = Button(window, text="Δημιουργία GUI", command=execute)
b1.grid(row=row)
row += 1

progress = Progressbar(window, orient=HORIZONTAL, length=200)
progress.grid(row=row)
row += 1

window.mainloop()
