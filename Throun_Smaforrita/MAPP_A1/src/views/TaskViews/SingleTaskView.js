import React from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, TouchableOpacity, Alert} from 'react-native';
import { withNavigation } from 'react-navigation';
import data from '../../resources/data.json';
import deleteTask from '../../services/TaskServices/DeleteTask'
import GlobalStyles from '../../styles/GlobalStyles';

// a conformaiton function for making sure the user want to delete the task
const deleteConformation = (Id, name, props, ListId, ListName) => {
    Alert.alert(
        'Do you want to delete the task:',
        name + '?',
        [
            {text: 'Yes', onPress: () => {deleteTask(Id, ListId, ListName, props)}},
            {text: 'No', style: 'cancel'},
        ],
        {
            cancelable: true
        }
    );
}

// the page rendered when the user wants to interact with a single task
const SingleTaskView = props => {
  // variables for keeping track of the user input so the board gets it's correct values
    var TaskDescription;
    var TaskName;
    var ListId;
    var Id;
    var ListName;
    var Status;
    var IsFinished;

    data.tasks.map((list) => {
        if(list.id == ListId) {
            ListName = list.name;
        }
    });
    return (
        <View style={GlobalStyles.container}>
            { data.tasks.map((task) => {
                if (task.id == props.navigation.state.params[0]) {

                    TaskDescription = task.description;
                    TaskName = task.name;
                    ListId = task.listId;
                    Id = task.id;
                    IsFinished = task.isFinished;
                    if (IsFinished == false) {
                        Status = 'Unfinished!'
                    } else {
                        Status = 'Completed!'
                    }

                    return (
                        <View key={task.id}>
                            <Text style={styles.Header}>
                                Task:{'\n'}{TaskName}
                            </Text>

                            <View style={styles.Item}>
                                <Text style={styles.TaskItem}>
                                    Description:{'\n  '}
                                    {TaskDescription}{'\n'}
                                </Text>

                                <Text style={styles.TaskItem}>
                                    Task status:{'\n  '}{Status}
                                </Text>
                            </View>
                        </View>
                    );
                }
            })}

            <Text style={styles.Header2}>
                Actions
            </Text>

            <View style={styles.Actions}>
                <TouchableOpacity style={GlobalStyles.ActionButton} onPress = {() => { props.navigation.navigate('ModifyTaskView', [Id, ListId, TaskName, TaskDescription, props.navigation.state.params[1], IsFinished])}}>
                    <Text style={GlobalStyles.ButtonText}>
                        Modify task
                    </Text>
                </TouchableOpacity>

                <TouchableOpacity style={GlobalStyles.ActionButton} onPress = {() => { props.navigation.navigate('MoveTaskView', [Id])}}>
                    <Text style={GlobalStyles.ButtonText}>
                        Move task
                    </Text>
                </TouchableOpacity>

                <TouchableOpacity style={GlobalStyles.ActionButton} onPress = {() => {deleteConformation(Id, TaskName, props, ListId, ListName)}}>
                    <Text style={GlobalStyles.ButtonText}>
                        Delete task
                    </Text>
                </TouchableOpacity>
            </View>
        <StatusBar style='auto' />
        </View>
    );
};

export default withNavigation(SingleTaskView);

const styles = StyleSheet.create({
    Header: {
        fontSize: 30,
        fontStyle: 'italic',
        fontWeight: 'bold',
        textAlign: 'center',
    },
    Header2: {
        color: '#ffffff',
        fontSize: 20,
        fontStyle: 'italic',
        fontWeight: 'bold',
        marginVertical: 4,
    },
    Item: {
        backgroundColor: '#eeeeee',
        borderWidth: 2,
        marginVertical: 40,
        width: 300,
    },
    TaskItem: {
        fontSize: 16,
        marginVertical: 8,
    },
});
