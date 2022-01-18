import React, { useState } from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, TouchableOpacity, TextInput, Alert } from 'react-native';
import data from '../../resources/data.json';
import GlobalStyles from '../../styles/GlobalStyles';
import modifyList from '../../services/ListServices/ModifyList';


// For reporting if all the fields are filled in or not.
var AllInputsFilledIn = (name) => {
    if (name.length > 0) {
      return true;
    }
    else {
      return false;
    }
}

// The page returned when wanting to modify an existing list
const ModifyListView = props => {
    // Keeping track of the user text input with the new list name
    const [name, setName] = useState(props.navigation.state.params[1]);
    // Finding the list which we are currently working with
    var ListId;
    data.lists.map((list) => {
        if(list.id == props.navigation.state.params[0]) {
            ListId = list.id;
        }
    });
    // The view returned when wanting to modify the list
    return (
        <View style={GlobalStyles.container}>
            <View>
                <Text style={styles.Header}>
                    Change name of list: {'\n'}{props.navigation.state.params[1]}
                </Text>
            </View>

            <View>
                <Text style={styles.BoxHeader}>
                    Enter new list name:
                </Text>

                <TextInput style={styles.Box} placeholder={props.navigation.state.params[1]} onChangeText={name => setName(name)} defaultValue={name}/>
            </View>

            <View style={styles.Confirmation}>
                <TouchableOpacity style={styles.ConfirmButton} onPress={() => { modifyList(ListId, name, props, props.navigation.state.params[2], props.navigation.state.params[3], props.navigation.state.params[4], AllInputsFilledIn(name)); props.navigation.navigate('SingleBoardView', [props.navigation.state.params[2], props.navigation.state.params[3], props.navigation.state.params[4], props])}}>
                    <Text style={styles.ConfirmText}>
                        Update list name
                    </Text>
                </TouchableOpacity>
            </View>
        <StatusBar style='auto' />
        </View>
    );
};

export default ModifyListView;

const styles = StyleSheet.create({
    Box: {
        backgroundColor: '#eeeeee',
        borderColor: '#000000',
        borderWidth: 3,
        height: 45,
        width: 300,
    },
    BoxHeader: {
        color: '#ffffff',
        fontSize: 14,
        fontWeight: 'bold',
        marginVertical: 16,
    },
    Confirmation: {
        alignContent: 'center',
    },
    ConfirmButton: {
        backgroundColor: '#000000',                        // 'lightgreen',
        borderColor: '#ffffff',
        borderWidth: 3,
        height: 40,
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
    Header: {
        fontSize: 28,
        fontStyle: 'italic',
        fontWeight: 'bold',
        marginVertical: 30,
        textAlign: 'center',
    },
});
