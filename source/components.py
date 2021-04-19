# You can add and edit components here.

def getButton():
    return """\t\t\t\t<Button
\t\t\t\t\tstyle={styles.button}
\t\t\t\t\ttitle="Button"
\t\t\t\t\tcolor="#f194ff"
\t\t\t\t\tonPress={() => Alert.alert("Button pressed!")}
\t\t\t\t/>"""


def getImage():
    return """\t\t\t\t<Image
\t\t\t\t\tstyle={styles.image}
\t\t\t\t\tsource={this.image}
\t\t\t\t/>"""


def getPressable():
    return """\t\t\t\t<Pressable 
\t\t\t\t\tstyle={styles.pressable}
\t\t\t\t\tonPress={() => { Alert.alert("Pressable pressed!")}}>
\t\t\t\t\t<Text> Pressable text </Text>
\t\t\t\t</Pressable>"""


def getSwitch():
    return """\t\t\t\t<Switch
\t\t\t\t\tstyle={styles.switch}
\t\t\t\t\ttrackColor={"#81b0ff"}
\t\t\t\t\tthumbColor={isEnabled ? "#f5dd4b" : "#f4f3f4"}
\t\t\t\t\tios_backgroundColor="#3e3e3e"
\t\t\t\t\tonValueChange={() => { Alert.alert("Switch pressed!") }}
\t\t\t\t\tvalue={0}
\t\t\t\t/>"""


def getText():
    return "\t\t\t\t<Text style={styles.text}> Plain text </Text>"


def getTextInput():
    return """\t\t\t\t<TextInput
\t\t\t\t\tstyle={styles.textInput}
\t\t\t\t\tonChangeText={() => { Alert.alert("TextInput changed!") }}
\t\t\t\t\tplaceholder="text input"
\t\t\t\t\tkeyboardType="numeric"
\t\t\t\t/>"""
