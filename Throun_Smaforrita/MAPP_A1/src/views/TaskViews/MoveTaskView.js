import React from 'react';
import { StyleSheet, Text, View, TouchableOpacity, TextInput, Alert, ScrollView } from 'react-native';
import data from '../../resources/data.json';
import GlobalStyles from '../../styles/GlobalStyles';
import MoveTask from '../../services/TaskServices/MoveTask';

// the page rendered when the user wants to move a task from one list to another
const MoveTaskView = props => {
    var TaskId;
    var ListId;
    // fertching the id's of that task
    { data.tasks.map((task) => {
        if ( task.id == props.navigation.state.params[0]) {
            TaskId = task.id;
            ListId = task.listId;
        }
    } );}

    return(
        <View style={GlobalStyles.container}>
            <ScrollView>
                <Text style={styles.Header}>
                    Move task to another list
                </Text>

                <Text style={styles.Instructions}>
                    Please select the list you want the task to be moved to
                </Text>

                <View style={styles.Boarder}>
                    {data.lists.map((list) => {
                            return (
                                <TouchableOpacity key={list.id} style={[styles.ListItem, {backgroundColor: list.color }]} onPress={() => { MoveTask(TaskId, list.id, props); props.navigation.navigate('ListView')}}>
                                    <Text style={styles.ListNameText}>
                                        {list.name}
                                    </Text>
                                </TouchableOpacity>
                            );
                    })}
                </View>
           </ScrollView>
        </View>
    )
}

export default MoveTaskView;

const styles = StyleSheet.create({
    Boarder: {
        alignItems: 'center',
        marginVertical: 10,
    },
    Header: {
        fontSize: 26,
        fontStyle: 'italic',
        fontWeight: 'bold',
        textAlign: 'center',
    },
    Instructions: {
        fontSize: 13,
        fontStyle: 'italic',
        marginVertical: 5,
        textAlign: 'center',
        top: 2,
    },
    ListItem: {
        borderColor: '#000000',
        borderWidth: 3,
        height: 40,
        marginVertical: 8,
        width: 200,
    },
    ListNameText: {
        fontSize: 14,
        fontWeight: 'bold',
        marginVertical: 5,
        textAlign: 'center',
    },
});
