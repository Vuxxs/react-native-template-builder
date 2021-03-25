# Μια γραμμή για αυτά πάνω κάτω, τα Touchable θα έχουν δικό τους section.
# Να μη ξεχάσουμε να βάλλουμε dummy values σε όσα χρειάζονται

def getActivityIndicator():
    return "<ActivityIndicator />"


def getButton():
    return """<Button
  onPress={() => console.log("Button pressed!")}
  title="Learn More"
  color="#841584"
  accessibilityLabel="Learn more about this purple button"
/>"""


def getFlatList():
    return """<FlatList
        data={DATA}
        renderItem={renderItem}
        keyExtractor={item => item.id}
      />"""


def getImage():
    return """<Image
        style={styles.image}
        source={require('@expo/snack-static/react-native-logo.png')}
      />"""


def getImageBackground():
    return """<ImageBackground source={image} style={styles.image}>
      <Text style={styles.text}>Inside</Text>
    </ImageBackground>"""


def getPressable():
    return """<Pressable onPress={onPressFunction}>
  <Text>I'm pressable!</Text>
</Pressable>"""


def getRefreshControl():
    return """<RefreshControl
            refreshing={refreshing}
            onRefresh={onRefresh}
          />"""


def getSectionList():
    return """<SectionList
      sections={DATA}
      keyExtractor={(item, index) => item + index}
      renderItem={({ item }) => <Item title={item} />}
      renderSectionHeader={({ section: { title } }) => (
        <Text style={styles.header}>{title}</Text>
      )}
    />"""


def getStatusBar():
    return """<StatusBar
        animated={true}
        backgroundColor="#61dafb"
        barStyle={statusBarStyle}
        showHideTransition={statusBarTransition}
        hidden={hidden} />"""


def getSwitch():
    return """<Switch
        trackColor={{ false: "#767577", true: "#81b0ff" }}
        thumbColor={isEnabled ? "#f5dd4b" : "#f4f3f4"}
        ios_backgroundColor="#3e3e3e"
        onValueChange={toggleSwitch}
        value={isEnabled}
      />"""


def getText():
    return "<Text style={styles.text}> </Text>"


def getTextInput():
    return """<TextInput
        style={styles.textInput}
        onChangeText={() => {console.log("text input changed")}}
        value={number}
        placeholder="useless placeholder"
        keyboardType="numeric"
      />"""


def getVirtualizedList():
    return """<VirtualizedList
        data={DATA}
        initialNumToRender={4}
        renderItem={({ item }) => <Item title={item.title} />}
        keyExtractor={item => item.key}
        getItemCount={getItemCount}
        getItem={getItem}
      />"""
