import React, { useState } from 'react';
import { StyleSheet, Text, View, TouchableOpacity, TextInput, Alert, Vibration } from 'react-native';
import { withNavigation } from 'react-navigation';
import addBoard from '../../services/BoardServices/AddBoard';
import GlobalStyles from '../../styles/GlobalStyles';


// For disabling the create board button, if there is something missinng within an input field
var AllInputsFilledIn = (name, photo) => {
    if (name.length > 0 && photo.length > 0 ) {
        return true;
    } else {
        return false;
    }
}
// the page rendered when wanting to create a new board
const AddNewBoardView = props => {
    // variables for keeping track of the user input so the board gets it's correct values
    const [name, setName] = useState('');
    const [thumbnailPhoto, setPhoto] = useState('');

    return (
        <View style={GlobalStyles.container}>
            <Text style={styles.Header}>
                Create New Board
            </Text>

            <Text style={styles.BoxText}>
                Enter board name:
            </Text>

            <TextInput placeholder=' Board name' style={styles.InputBox} onChangeText={name => setName(name)} defaultValue={name}/>

            <Text style={styles.BoxText}>
                {'\n'}Enter photo URL:
            </Text>

            <TextInput placeholder=' Board thumbnail photo URL' style={styles.InputBox} onChangeText={thumbnailPhoto => setPhoto(thumbnailPhoto)} defaultValue={thumbnailPhoto}/>

            <TouchableOpacity style={styles.ConfirmButton} onPress={() => { addBoard(name, thumbnailPhoto, AllInputsFilledIn(name, thumbnailPhoto)); props.navigation.navigate('BoardListView', props)}}>
                <Text style={styles.ButtonText}>
                    Create the board
                </Text>
            </TouchableOpacity>
        </View>
    );
};

export default withNavigation(AddNewBoardView);

const styles = StyleSheet.create({
    BoxText: {
        backgroundColor: '#42638E',                   // '#feffa3',
        color: '#ffffff',
        fontSize: 16,
        fontWeight: 'bold',
    },
    ButtonText: {
        alignContent: 'center',
        color: '#ffffff',
        fontSize: 14,
        fontWeight: 'bold',
        marginVertical: 7,
        textAlign: 'center',
    },
    ConfirmButton: {
        alignItems: 'center',
        backgroundColor: '#000000',                   // 'lightgreen',
        borderColor: '#ffffff',
        borderWidth: 2,
        height: 40,
        marginVertical: 50,
        width: 180,
    },
    Header: {
        fontSize: 28,
        fontStyle: 'italic',
        fontWeight: 'bold',
        marginVertical: 20,
    },
    InputBox: {
        alignItems: 'center',
        backgroundColor: '#eeeeee',
        height: 40,
        marginVertical: 12,
        width: 220,
    },
});
