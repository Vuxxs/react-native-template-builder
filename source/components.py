# You can add and edit components here.

def getButton():
    return """<Button
                    title="Press me"
                    color="#f194ff"
                    onPress={() => Alert.alert("Button pressed!")}
                />"""


def getImage():
    return """<Image
                    style={styles.image}
                    source={this.image}
                />"""


def getPressable():
    return """<Pressable onPress={() => {
                    Alert.alert("Pressable pressed!");
                }}>
                    <Text> Pressable text </Text>
                </Pressable>"""


def getSwitch():
    return """<Switch
                    trackColor={"#81b0ff"}
                    thumbColor={isEnabled ? "#f5dd4b" : "#f4f3f4"}
                    ios_backgroundColor="#3e3e3e"
                    onValueChange={() => { Alert.alert("Switch pressed!") }}
                    value={0}
                />"""


def getText():
    return "<Text style={styles.text}> Plain text </Text>"


def getTextInput():
    return """<TextInput
                    style={styles.textInput}
                    onChangeText={() => { Alert.alert("TextInput changed!") }}
                    placeholder="text input"
                    keyboardType="numeric"
                />"""
