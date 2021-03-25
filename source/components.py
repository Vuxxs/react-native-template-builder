# Μια γραμμή για αυτά πάνω κάτω, τα Touchable θα έχουν δικό τους section.
# Να μη ξεχάσουμε να βάλλουμε dummy values σε όσα χρειάζονται

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
                    trackColor={{ false: "#767577", true: "#81b0ff" }}
                    thumbColor={isEnabled ? "#f5dd4b" : "#f4f3f4"}
                    ios_backgroundColor="#3e3e3e"
                    onValueChange={() => { Alert.alert("Switch pressed!") }}
                    value={isEnabled}
                />"""


def getText():
    return "<Text style={styles.text}> Plain text </Text>"


def getTextInput():
    return """<TextInput
                    style={styles.textInput}
                    onChangeText={() => { Alert.alert("TextInput changed!") }}
                    value={10}
                    placeholder="useless placeholder"
                    keyboardType="numeric"
                />"""
