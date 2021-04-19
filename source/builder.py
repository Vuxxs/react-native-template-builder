# This is the template building script.
# Every phase is separated and made easy to edit if you are trying to generate templates based on your preference.

import os
from random import randrange
from source.components import *


def buildTemplate(numOfComponents):
    # Initialization phase
    template = ""

    # Pick a random template
    files = os.listdir("./templates/Views")
    f = open("./templates/Views/" + str(randrange(len(files)) + 1))
    template += f.read()
    f.close()

    template += "\n\n"
    # Place Random Components
    components = [getButton(), getImage(), getPressable(),
                  getSwitch(), getText(), getTextInput()]
    for x in range(numOfComponents):
        componentPicked = components[randrange(len(components))]
        template += componentPicked + "\n\n"

    # You might want to remove this if you need a component to be in the bottom.
    template += """\t\t\t</View>
        );
    }
}\n\n"""
    files = os.listdir("./templates/Stylesheets/")
    f = open("./templates/Stylesheets/" + str(randrange(len(files)) + 1))
    template += f.read()
    f.close()
    # Append the stylesheet and finish the process

    # Write to file
    f = open("Template.js", "w")
    f.write(template)
    f.close()
