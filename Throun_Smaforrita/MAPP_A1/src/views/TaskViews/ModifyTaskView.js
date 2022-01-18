import React, { useState } from 'react';
import { StyleSheet, Text, View, TouchableOpacity, TextInput, Alert } from 'react-native';
import data from '../../resources/data.json';
import GlobalStyles from '../../styles/GlobalStyles';
import modifyTask from '../../services/TaskServices/ModifyTask'


// For reporting, if all the fields are filled in (or not).
var AllInputsFilledIn = (name, description) => {
    if (name.length > 0 && description.length > 0 ) {
        return true;
    } else {
        return false;
    }
}

// This is the page view where you can modify an existing task
const ModifyExistingTaskView = props => {
    // Keep track of variables nessecary for updting the task correctly
    const [name, setName] = useState(props.navigation.state.params[2]);
    const [description, setDescription] = useState(props.navigation.state.params[3]);
    const [isFinished, setIsFinished] = useState(props.navigation.state.params[5]);
    // Initializing a variable for tracking which status button is currently pressed
    var currentButton;
    // to initialize the correct button upon entering the page, so that if the task
    // is not complete the button "Not completed will be on by default"
    if (isFinished) {
        currentButton = 'Button1';
    } else{
        currentButton = 'Button2';
    }
    const [selectedButton, setSelectedButton] = useState(currentButton);

    // Variable for the navigate function so that the correct list name gets passed back to the list view
    var ListName = '';
    // Finding the correct list name
    data.lists.map((list) => {
        if(list.id == props.navigation.state.params[4]) {
            ListName = list.name;
        }
    });

    // The view which is returned for modifying the task
    return (
        <View style={GlobalStyles.container}>
            <Text style={styles.Header}>
                Modify task:{'\n'}{props.navigation.state.params[2]}
            </Text>

            <Text style={styles.Details}>
                All fields need to be filled in in order to modify a task:{'\n\n'}
            </Text>

            <Text style={styles.InputHeader}>
                Enter updated task name:
            </Text>

            <TextInput style={styles.BoxInput} placeholder={props.navigation.state.params[2]} onChangeText={name => setName(name)} defaultValue={name}/>

            <Text style={styles.InputHeader}>
                Enter updated description:
            </Text>

            <TextInput style={styles.BoxInput} placeholder={props.navigation.state.params[3]} onChangeText={description => setDescription(description)} defaultValue={description}/>

            <Text style={styles.InputHeader}>
                Task Status:
            </Text>

            <TouchableOpacity style={currentButton=='Button1' ? styles.CurrentButton: styles.NotCurrentButton} onPress={() => {setIsFinished(true); setSelectedButton('Button1')}}>
                <Text style={styles.TaskStatus}>
                    Completed
                </Text>
            </TouchableOpacity>

            <TouchableOpacity style={currentButton=='Button2' ? styles.CurrentButton: styles.NotCurrentButton} onPress={() => {setIsFinished(false); setSelectedButton('Button2')}}>
                <Text style={styles.TaskStatus}>
                    Not completed
                </Text>
            </TouchableOpacity>

            <TouchableOpacity style={styles.Button} onPress={() => { modifyTask(props.navigation.state.params[0], name, description, props.navigation.state.params[1], isFinished, AllInputsFilledIn(name, description)); props.navigation.navigate('ListView', [props.navigation.state.params[1], ListName])}}>
                <Text style={styles.ButtonText}>
                    Update the task
                </Text>
            </TouchableOpacity>
        </View>
    );
};

export default ModifyExistingTaskView;

const styles = StyleSheet.create({
    BoxInput: {
        backgroundColor: '#eeeeee',
        height: 40,
        width: 300,
    },
    Button: {
        backgroundColor: '#000000',
        borderColor: '#ffffff',
        borderWidth: 3,
        height: 40,
        marginVertical: 30,
        width: 160,
    },
    ButtonText: {
        color: '#ffffff',
        fontSize: 16,
        fontWeight: 'bold',
        marginVertical: 6,
        textAlign: 'center',
    },
    CurrentButton: {
        backgroundColor: '#ffffff',
        borderWidth: 2,
        height: 30,
        marginVertical: 3,
        width: 140,
    },
    Details: {
        fontSize: 14,
        fontStyle: 'italic',
        textAlign: 'center',
    },
    Header: {
        fontSize: 30,
        fontStyle: 'italic',
        fontWeight: 'bold',
        textAlign: 'center',
    },
    InputHeader: {
        color: '#ffffff',
        fontSize: 16,
        fontWeight: 'bold',
        marginVertical: 10,
    },
    NotCurrentButton: {
        backgroundColor: 'darkgrey',
        borderWidth: 2,
        height: 30,
        marginVertical: 3,
        width: 140,
    },
    TaskStatus: {
        fontSize: 13,
        fontWeight: 'bold',
        marginVertical: 4,
        textAlign: 'center',
    },
});
