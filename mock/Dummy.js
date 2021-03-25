import React, { Component } from 'react';
import { View, StyleSheet, Alert } from 'react-native';
import { Button, Image, Pressable, Switch, Text, TextInput } from 'react-native';

export default class Template extends Component {

    image = require('./../dump/sample.jpg');
    render() {
        return (
            <View style={styles.container}>
                <Button
                    title="Press me"
                    color="#f194ff"
                    onPress={() => Alert.alert("Button pressed!")}
                />

                <Image
                    style={styles.image}
                    source={this.image}
                />

                <Pressable onPress={() => {
                    Alert.alert("Pressable pressed!");
                }}>
                    <Text> Pressable text </Text>
                </Pressable>

                <Switch
                    trackColor={{ false: "#767577", true: "#81b0ff" }}
                    thumbColor={isEnabled ? "#f5dd4b" : "#f4f3f4"}
                    ios_backgroundColor="#3e3e3e"
                    onValueChange={() => { Alert.alert("Switch pressed!") }}
                    value={isEnabled}
                />

                <Text style={styles.text}> Plain text </Text>

                <TextInput
                    style={styles.textInput}
                    onChangeText={() => { Alert.alert("TextInput changed!") }}
                    value={10}
                    placeholder="useless placeholder"
                    keyboardType="numeric"
                />
            </View>
        );
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 10,
        backgroundColor: "#FFFFFF",
    },

    image: {
        width: 100,
        height: 100
    },

    text: {
        fontSize: 25,
        fontWeight: "bold"
    },

    textInput: {
        height: 100,
        margin: 100,
        borderWidth: 5
    }
});