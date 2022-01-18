import React, { useState } from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, TouchableOpacity, TextInput, Alert, Vibration } from 'react-native';
import * as FileSystem from 'expo-file-system';
import addTask from '../../services/TaskServices/AddTask';
import data from '../../resources/data.json';
import GlobalStyles from '../../styles/GlobalStyles';


// Specifying vibration duration
const VIBE_SEC = 1500;      // milliseconds --> 1.5 sec

// For disabling the create list button, if there are any input fields empty
var AllInputsFilledIn = (name, description) => {
    if (name.length > 0 && description.length > 0 ) {
        return true;
    } else {
        return false;
    }
}

// The page rendered when wanting to add a new board
const AddNewTaskView = props => {
    // Variables for keeping track of the text input information from the user
    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
    const [isFinished, setIsFinished] = useState(props.navigation.state.params[5]);

    // Keep track of which status button is currently pressed
    var currentButton;
    if (isFinished) {
        currentButton = 'Button1';
    }
    else{
        currentButton = 'Button2';
    }
    const [selectedButton, setSelectedButton] = useState(currentButton);

    // The view returned when entering the page
    return (
        <View style={GlobalStyles.container}>
            <View>
                <Text style={styles.Header}>
                    New task for list:{'\n'}{props.navigation.state.params[1]}
                </Text>
            </View>

            <View>
                <Text style={styles.BoxHeader}>
                    Enter task name:
                </Text>

                <TextInput style={styles.Box} placeholder='  Task name' onChangeText={name => setName(name)} defaultValue={name}/>

                <Text style={styles.BoxHeader}>
                    Enter task description:
                </Text>

                <TextInput style={styles.Box} placeholder='  Task Description' onChangeText={description => setDescription(description)} defaultValue={description}/>
            </View>

            <View style={styles.Confirmation}>
                <TouchableOpacity style={styles.ConfirmButton} onPress={() => { addTask(name, description, props.navigation.state.params[0], AllInputsFilledIn(name, description)); props.navigation.navigate('ListView', [props.navigation.state.params[0], props.navigation.state.params[1]])}}>
                    <Text style={styles.ConfirmText}>
                        Create the task
                    </Text>
                </TouchableOpacity>
            </View>
        <StatusBar style='auto' />
       </View>
    );
};

export default AddNewTaskView;

const styles = StyleSheet.create({
    Box: {
        backgroundColor: '#eeeeee',
        borderWidth: 2,
        height: 40,
        width: 300,
    },
    BoxHeader: {
        color: '#ffffff',
        fontSize: 16,
        fontWeight: 'bold',
        marginVertical: 14,
    },
    Confirmation: {
        alignContent: 'center',
    },
    ConfirmButton: {
        backgroundColor: '#000000',                    // 'lightgreen',
        borderColor: '#ffffff',
        borderWidth: 3,
        height: 40,
        marginVertical: 40,
        width: 150,
    },
    ConfirmText: {
        color: '#ffffff',
        fontSize: 16,
        fontWeight: 'bold',
        marginVertical: 4,
        textAlign: 'center',
    },
    Header: {
        fontSize: 30,
        fontStyle: 'italic',
        fontWeight: 'bold',
        marginVertical: 30,
        textAlign: 'center',
    },
});
