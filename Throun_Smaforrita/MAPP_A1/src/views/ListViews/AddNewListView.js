import React, { useState } from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, TouchableOpacity, TextInput, Alert, Vibration } from 'react-native';
import * as FileSystem from 'expo-file-system';
import addList from '../../services/ListServices/AddList';
import data from '../../resources/data.json';
import GlobalStyles from '../../styles/GlobalStyles';


const VIBE_SEC = 1500;      // milliseconds --> 1.5 sec

// For disabling the create list button, if there are any input fields missing
var NameFilledIn = (name) => {
    if (name.length > 0) {
        return true;
    } else {
        return false;
    }
}
// the page rendered when wanting to add a new list to a board
const AddNewListView = props => {
  // variables for keeping track of the user input so the list gets it's correct values
    const [name, setName] = useState('');
    return (
        <View style={GlobalStyles.container}>
            <View style={styles.BoardName}>
                <Text style={styles.Header}>
                    New list for board:{'\n'}{props.navigation.state.params[1]}
                </Text>
            </View>

            <View style={styles.NewListInfo}>
                <Text style={styles.NewListName}>
                    Enter list name:
                </Text>

                <TextInput style={styles.ListNameInputBox} placeholder=' List name' onChangeText={name => setName(name)} defaultValue={name}/>

                <TouchableOpacity style={styles.CreateListButton} onPress={() => { addList(name, props.navigation.state.params[0], NameFilledIn(name)); props.navigation.navigate('SingleBoardView', [props.navigation.state.params[0], props.navigation.state.params[1]])}}>
                    <Text style={styles.ButtonText}>
                        Create the list
                    </Text>
                </TouchableOpacity>
            </View>
        <StatusBar style='auto' />
        </View>
    );
};

export default AddNewListView;

const styles = StyleSheet.create({
    BoardName: {
        flex: 2,
    },
    ButtonText: {
        color: '#ffffff',
        fontSize: 16,
        fontWeight: 'bold',
        marginVertical: 4,
        textAlign: 'center',
    },
    CreateListButton: {
        alignItems: 'center',
        backgroundColor: '#000000',                        // 'lightgreen',
        borderColor: '#ffffff',
        borderWidth: 3,
        height: 40,
        left: 30,
        marginVertical: 40,
        width: 180,
    },
    Header: {
        fontSize: 26,
        fontStyle: 'italic',
        fontWeight: 'bold',
        marginVertical: 10,
        textAlign: 'center',
    },
    ListNameInputBox: {
        alignItems: 'center',
        backgroundColor: '#eeeeee',
        borderWidth: 1,
        height: 40,
        marginVertical: 10,
        width: 250,
    },
    NewListInfo: {
        flex: 10,
    },
    NewListName: {
        fontSize: 18,
        fontWeight: 'bold',
        marginVertical: 5,
    },
});
