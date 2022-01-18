import React, { useState } from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, TouchableOpacity, TextInput, Alert } from 'react-native';
import * as FileSystem from 'expo-file-system';
import data from '../../resources/data.json';
import GlobalStyles from '../../styles/GlobalStyles';
import modifyBoard from '../../services/BoardServices/ModifyBoard';


// For reporting if all the fields are filled in or not.
var AllInputsFilledIn = (name, thumbnailPhoto) => {
    if (name.length > 0 && thumbnailPhoto.length > 0 ) {
      return true;
    }
    else {
      return false;
    }
}

// the page rendered when wanting to modify an existing board
const ModifyBoardView = props => {
    // variables for keeping track of the user input so the board gets it's correct values
    const [name, setName] = useState(props.navigation.state.params[1]);
    const [thumbnailPhoto, setThumbnailPhoto] = useState(props.navigation.state.params[2]);
    var BoardId;
    // seeing if the id is in our data
    data.boards.map((board) => {
        if(board.id == props.navigation.state.params[0]) {
            BoardId = board.id;
        }
    });
    return (
        <View style={GlobalStyles.container}>
            <View>
                <Text style={styles.Header}>
                    Modify board: {'\n'}{props.navigation.state.params[1]}
                </Text>
            </View>

            <View>
                <Text style={styles.BoxHeader}>
                    Update board name:
                </Text>

                <TextInput style={styles.Box} placeholder={props.navigation.state.params[1]} onChangeText={name => setName(name)} defaultValue={name}/>

                <Text style={styles.BoxHeader}>
                    Updated photo URL:
                </Text>

                <TextInput style={styles.Box} placeholder={props.navigation.state.params[2]} onChangeText={thumbnailPhoto => setThumbnailPhoto(thumbnailPhoto)} defaultValue={thumbnailPhoto}/>

                <TouchableOpacity style={styles.ConfirmButton} onPress={() => { modifyBoard(BoardId, name, thumbnailPhoto, props, AllInputsFilledIn(name, thumbnailPhoto));props.navigation.navigate('BoardListView', props)}}>
                    <Text style={styles.ConfirmText}>
                        Update the board
                    </Text>
                </TouchableOpacity>
            </View>
        <StatusBar style='auto' />
        </View>
    );
};

export default ModifyBoardView;

const styles = StyleSheet.create({
    Box: {
        backgroundColor: '#eeeeee',
        borderWidth: 1,
        height: 45,
        width: 200,
    },
    BoxHeader: {
        fontSize: 16,
        fontWeight: 'bold',
        marginVertical: 12,
    },
    ConfirmButton: {
        backgroundColor:'#000000',                    // 'lightgreen',
        borderColor: '#ffffff',
        borderWidth: 3,
        height: 40,
        left: 30,
        marginVertical: 40,
        width: 140,
    },
    ConfirmText: {
        color: '#ffffff',
        fontSize: 14,
        fontWeight: 'bold',
        marginVertical: 6,
        textAlign: 'center',
    },
    Header: {
        color: '#ffffff',
        fontSize: 26,
        fontStyle: 'italic',
        fontWeight: 'bold',
        marginBottom: 20,
        textAlign: 'center',
    },
});
