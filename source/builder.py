# This is the template building script.
# Every phase is separated and made easy to edit if you are trying to generate templates based on your preference.

import os
from random import randrange, shuffle
from source.components import *
from source.makeStylesheet import makeStylesheet


def getRandomFile(dir):
    files = os.listdir("./templates/" + dir)
    f = open("./templates/" + dir + str(randrange(len(files)) + 1))
    return f.read()


def buildTemplate(num_text, num_text_input, num_switch, num_pressable, num_image, num_button):
    component_list = []
    for i in range(num_text):
        component_list.append(getText())
    for i in range(num_text_input):
        component_list.append(getTextInput())
    for i in range(num_switch):
        component_list.append(getSwitch())
    for i in range(num_pressable):
        component_list.append(getPressable())
    for i in range(num_image):
        component_list.append(getImage())
    for i in range(num_button):
        component_list.append(getButton())

    shuffle(component_list)

    # Initialization phase
    template = ""

    # Pick a random template
    template += getRandomFile("Views/Top/")

    template += "\n\n"

    f = open("./templates/Stylesheets/Random", "w")
    head = open("./templates/Stylesheets/Head")
    f.write(head.read())
    head.close()
    f.close()

    for component in component_list:
        # componentPicked = components[randrange(len(components))]()
        template += component[0] + "\n\n"
        makeStylesheet(component[1])

    # You might want to remove this if you need a component to be in the bottom.
    template += getRandomFile("Views/Bottom/")
    template += "\n\n"

    f = open("./templates/Stylesheets/Random")
    template += f.read() + "});"
    # Append the stylesheet and finish the process

    # Write to file
    files = os.listdir("./generated/")
    f = open("./generated/Template_" +
             str(len(files) + 1) + ".js", "w")
    f.write(template)
    f.close()
