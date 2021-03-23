# Μια γραμμή για αυτά πάνω κάτω, τα Touchable θα έχουν δικό τους section.

def getText():
    return "<Text style={styles.text}> </Text>"

const App = () => (
  <View style={[styles.container, styles.horizontal]}>
    <ActivityIndicator />
    <ActivityIndicator size="large" />
    <ActivityIndicator size="small" color="#0000ff" />
    <ActivityIndicator size="large" color="#00ff00" />
  </View>
);

<View>
      <Text style={styles.container}>
        The title and onPress handler are required. It is recommended to set accessibilityLabel to help make your app usable by everyone.
      </Text>
      <Button
        title="Press me"
        onPress={() => Alert.alert('Simple Button pressed')}
      />
    </View>

 <View style={styles.item}>
    <Text style={styles.item}>{title}</Text>
  </View>

    <View style={styles.container}>
      <Image
        style={styles.container}
        source={require('@expo/snack-static/react-native-logo.png')}
      />
      <Image
        style={styles.container}
        source={{
          uri: 'https://reactnative.dev/img/tiny_logo.png',
        }}
      />
      <Image
        style={styles.logo}
        source={{
          uri: 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADMAAAAzCAYAAAA6oTAqAAAAEXRFWHRTb2Z0d2FyZQBwbmdjcnVzaEB1SfMAAABQSURBVGje7dSxCQBACARB+2/ab8BEeQNhFi6WSYzYLYudDQYGBgYGBgYGBgYGBgYGBgZmcvDqYGBgmhivGQYGBgYGBgYGBgYGBgYGBgbmQw+P/eMrC5UTVAAAAABJRU5ErkJggg==',
        }}
      />
    </View>

<View style={styles.container}>
    <ImageBackground source={image} style={styles.image}>
      <Text style={styles.text}>Inside</Text>
    </ImageBackground>
  </View>

  <ScrollView
        contentContainerStyle={styles.scrollView}
        refreshControl={
          <RefreshControl
            refreshing={refreshing}
            onRefresh={onRefresh}
          />
        }
      >
        <Text>Pull down to see RefreshControl indicator</Text>
     </ScrollView>

<View style={styles.item}>
    <Text style={styles.item}>{title}</Text>
  </View>

  <View style={styles.buttonsContainer}>
        <Button
          title="Toggle StatusBar"
          onPress={changeStatusBarVisibility} />
        <Button
          title="Change StatusBar Style"
          onPress={changeStatusBarStyle} />
        {Platform.OS === 'ios' ? (
          <Button
            title="Change StatusBar Transition"
            onPress={changeStatusBarTransition} />
        ) : null}
      </View>

     <View style={styles.container}>
      <Switch
        trackColor={{ false: "#767577", true: "#81b0ff" }}
        thumbColor={isEnabled ? "#f5dd4b" : "#f4f3f4"}
        ios_backgroundColor="#3e3e3e"
        onValueChange={toggleSwitch}
        value={isEnabled}
      />
    </View>

    <View style={styles.container}>
      <View style={styles.countContainer}>
        <Text>Count: {count}</Text>
      </View>
      <TouchableOpacity
        style={styles.button}
        onPress={onPress}
      >
        <Text>Press Here</Text>
      </TouchableOpacity>
    </View>

     <View style={styles.item}>
    <Text style={styles.item}>{title}</Text>
  </View>