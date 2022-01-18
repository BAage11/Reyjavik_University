import React, { useState } from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, TouchableOpacity, TextInput, Alert } from 'react-native';
import data from '../../resources/data.json';
import GlobalStyles from '../../styles/GlobalStyles';
import ListColorPicker from '../../components/ListComponents/ListColorPicker';
import modifyColorList from '../../services/ListServices/ModifyColorList';


// The page rendered when wanting to chagne the name of a list
const ModifyListColorView = (props) => {
    // Variables for keeping track of user input to change the color correctly
    const [color, setColor] = useState(props.navigation.state.params[2]);

    // Finding the correct list id to send back with the navigate function
    var ListId;
    data.lists.map((list) => {
        if(list.id == props.navigation.state.params[0]) {
            ListId = list.id;
        }
    });
    return (
        <View style={GlobalStyles.container}>
            <View>
                <Text style={styles.Header}>
                    Change colour of list: {'\n'}{props.navigation.state.params[1]}
                </Text>
            </View>

            <ListColorPicker listId={ListId} boardId={props.navigation.state.params[2]} boardName={props.navigation.state.params[3]} thumbnail={props.navigation.state.params[4]} props={props}>
            </ListColorPicker>
        <StatusBar style='auto' />
        </View>
    );
};

export default ModifyListColorView;

const styles = StyleSheet.create({
    Box: {
        backgroundColor: '#eeeeee',
        borderWidth: 3,
        height: 45,
        textAlign: 'center',
        width: 200,
    },
    BoxHeader: {
        color: '#ffffff',
        fontSize: 18,
        fontWeight: 'bold',
        marginVertical: 16,
        right: 5,
        textAlign: 'center',
        top: 10,
    },
    ConfirmButton: {
        backgroundColor: "#000000",
        borderColor: '#ffffff',
        borderWidth: 3,
        height: 40,
        left: '30%',
        marginVertical: 40,
        width: 160,
    },
    ConfirmText: {
        color: '#ffffff',
        fontSize: 16,
        fontWeight: 'bold',
        marginVertical: 6,
        textAlign: 'center',
    },
    FurtherInformation: {
        fontSize: 12,
        fontStyle: "italic",
        marginVertical: 14,
        textAlign: 'center',
    },
    Header: {
        fontSize: 28,
        fontStyle: 'italic',
        fontWeight: 'bold',
        textAlign: 'center',
    },
    Link: {
        fontStyle: "normal",
        fontWeight: 'bold',
    },
    UserInput: {
        alignItems: 'center',
        marginVertical: 14,
    },
});
