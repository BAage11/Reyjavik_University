import React from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, ScrollView, TouchableOpacity, Alert } from 'react-native';
import data from '../../resources/data.json';
import deleteList from '../../services/ListServices/DeleteList';
import GlobalStyles from '../../styles/GlobalStyles';
import TaskListComponent from '../../components/TaskComponents/TaskListComponent';

// alert with a conformation question to be sure the user wants to delete
const deleteConformation = (Id, name, props) => {
    Alert.alert(
        'Do you want to delete the list:',
        name + '?',
        [
            {text: 'Yes', onPress: () => {deleteList(Id, props)}},
            {text: 'No', style: 'cancel'},
        ],
        {
            cancelable: true
        }
    );
}

// the page rendered when the used wants to intereact with a list
const ListView = (props) => {
    return (
        <View style={GlobalStyles.container}>
            <Text style={styles.Header}>
                {props.navigation.state.params[1]}
            </Text>

            <ScrollView style={styles.Lists}>
                { data.tasks.map((task) => {
                    if ( task.listId == props.navigation.state.params[0]) {
                        return (
                            <View style={ styles.TaskItem} key={task.id}>
                                <TaskListComponent listId={task.listId} id={task.id} name={task.name} description={task.description} isFinished={task.isFinished}/>
                            </View>
                        );
                    }
                })}
            </ScrollView>

            <Text style={styles.Header2}>
                Actions
            </Text>

            <TouchableOpacity style={GlobalStyles.ActionButton} onPress={() => props.navigation.navigate('AddNewTaskView', [props.navigation.state.params[0], props.navigation.state.params[1]])}>
                <Text style={GlobalStyles.ButtonText}>
                    New task
                </Text>
            </TouchableOpacity>

            <TouchableOpacity style={GlobalStyles.ActionButton} onPress={() => props.navigation.navigate('ModifyListView', [props.navigation.state.params[0], props.navigation.state.params[1], props.navigation.state.params[2], props.navigation.state.params[3], props.navigation.state.params[4]])}>
                <Text style={GlobalStyles.ButtonText}>
                    Change list name
                </Text>
            </TouchableOpacity>

            <TouchableOpacity style={GlobalStyles.ActionButton} onPress={() => props.navigation.navigate('ModifyListColourView', [props.navigation.state.params[0], props.navigation.state.params[1], props.navigation.state.params[2], props.navigation.state.params[3], props.navigation.state.params[4]])}>
                <Text style={GlobalStyles.ButtonText}>
                    Change list colour
                </Text>
            </TouchableOpacity>

            <TouchableOpacity style={GlobalStyles.ActionButton} onPress={() => deleteConformation(props.navigation.state.params[0], props.navigation.state.params[1], props)}>
                <Text style={GlobalStyles.ButtonText}>
                    Delete list
                </Text>
            </TouchableOpacity>
            <StatusBar style='auto' />
        </View>
    );
};

export default ListView;

const styles = StyleSheet.create({
    Header: {
        fontSize: 34,
        fontStyle: 'italic',
        fontWeight: 'bold',
        marginVertical: 10,
    },
    Header2: {
        color: '#ffffff',
        fontSize: 20,
        fontStyle: 'italic',
        fontWeight: 'bold',
        marginVertical: 5,
    },
});
