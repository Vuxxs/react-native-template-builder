# Μια γραμμή για αυτά πάνω κάτω, τα Touchable θα έχουν δικό τους section.

def getText():
  return "<Text style={styles.text}> </Text>"

def getButton():
  return """<Button
  onPress={() => {}}
  title="Learn More"
  color="#841584"
  accessibilityLabel="Learn more about this purple button"
/>"""
 

def getImage():
  return """<Image
    style={styles.containers}
    source="@expo/snack-static/react-native-logo.png"
/>"""

def getImageBackground():
  return  """ImageBackground
  source = {image}
  style = {styles.containers}
  />"""

def getSectionList():
  return "<SectionList style={styles.title}>{title}</SectionList>"

def getStatusBar():
  return """<StatusBar
    onPress={() => {}}
    title="Toggle StatusBar"
    />"""

def getTouchableHighlight():
  return """TouchableHighlight
      onPress={( => {})}
      style={styles.container}
      title="Touch Here"
      />"""

def getVirtualizedList():
  return "<VirtualizedList style={styles.item>{item}</VirtualizedList style>"
