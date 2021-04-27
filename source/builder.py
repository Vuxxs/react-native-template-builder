# This is the template building script.
# Every phase is separated and made easy to edit if you are trying to generate templates based on your preference.

import os
from random import randrange
from source.components import *
from source.makeStylesheet import makeStylesheet


def getRandomFile(dir):
    files = os.listdir("./templates/" + dir)
    f = open("./templates/" + dir + str(randrange(len(files)) + 1))
    return f.read()


def buildTemplate(numOfComponents):
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

    # Place Random Components
    components = [getButton, getImage, getPressable,
                  getSwitch, getText, getTextInput]

    for x in range(numOfComponents):
        componentPicked = components[randrange(len(components))]()
        template += componentPicked[0] + "\n\n"
        makeStylesheet(componentPicked[1])

    # You might want to remove this if you need a component to be in the bottom.
    template += getRandomFile("Views/Bottom/")
    template += "\n\n"

    f = open("./templates/Stylesheets/Random")
    template += f.read() + "});"
    # Append the stylesheet and finish the process

    # Write to file
    files = os.listdir("./Generated Templates/")
    f = open("./Generated Templates/Template_" +
             str(len(files) + 1) + ".js", "w")
    f.write(template)
    f.close()
