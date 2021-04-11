# This is the template building script.
# Every phase is separated and made easy to edit if you are trying to generate templates based on your preference.

from random import randrange
from source.components import getButton, getImage, getPressable, getSwitch, getText, getTextInput


def buildTemplate():
    # Initialization phase
    template = """import React, { Component } from 'react';
    import { View, StyleSheet, Alert } from 'react-native';
    import { Button, Image, Pressable, Switch, Text, TextInput } from 'react-native';\n"""

    # Generate default class
    template += """export default class Template extends Component {

        image = require('./../dump/sample.jpg');
        render() {
            return (\n"""

    # Generate View, the reason this isn't grouped up with default class is so you can change the View type if you choose to.
    template += "<View style={styles.container}>\n"

    # Randomization phase

    # Pick a random template and draw from './../templates/...'

    templates = ["Import files as an array from ./../templates/UI"]
    stylesheets = ["Import files as an array from ./../templates/SS"]

    # Pick one of each randomly
    templatePicked = templates[randrange(len(templates))]
    stylesheetPicked = stylesheets[randrange(len(stylesheets))]

    # Replace component code (#0000) with random component
    components = ["button", "image", "pressable",
                  "switch", "text", "textInput"]
    while("0000" in templatePicked):
        position = templatePicked.index("0000")
        componentPicked = components[randrange(len(components))]
        templatePicked = templatePicked[:position] + \
            componentPicked + templatePicked[position+1:]

    # Place components to the positions defined

    for component in components:
        while(component in templatePicked):
            print("Found " + component + "! Replacing it appropriately..")
            position = templatePicked.index(component)
            templatePicked = templatePicked[:position] + \
                component + templatePicked[position+1:]

    # Append the ready-to-go template
    template += templatePicked + "\n"
    template += """</View>
            );
        }
    }\n"""

    # Append the stylesheet and finish the process
    template += stylesheetPicked

    # Write to file
    f = open("Template.js", "w")
    f.write(template)
    f.close()
