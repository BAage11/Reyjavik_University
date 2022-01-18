import React, {useRef} from 'react';
import { StyleSheet, Text, View, TouchableOpacity } from 'react-native';
import { withNavigation } from 'react-navigation';

// this is a component used for the ListView where each task in the list is made of this component
const TaskListComponent = (props) => {
    // a variable to display whether the task is  finished or not
    var Status;
    if (props.isFinished == false) {
        Status = 'Unfinished!'
    } else {
        Status = 'Completed!'
    }
    return (
        <TouchableOpacity style={styles.TaskItem} onPress={() => props.navigation.navigate('SingleTaskView', [props.id, props.name, props.listId])}>
            <Text style={styles.TaskItemText}>
                Task name:  {props.name}
            </Text>

            <Text style={styles.Descript}>
                {" "}{props.description}
            </Text>

            <Text style={styles.TaskItemText}>
                Status of task:  {Status}
            </Text>
        </TouchableOpacity>
    )
};

export default withNavigation(TaskListComponent);

const styles = StyleSheet.create({
    Descript: {
        fontStyle: 'italic',
    },
    TaskItem: {
        alignItems: 'flex-start',
        backgroundColor: '#D8FAF5',
        borderColor: '#ffffff',
        borderWidth: 3,
        height: 100,
        marginVertical: 10,
        width: 300,
    },
    TaskItemText: {
        fontSize: 14,
        fontWeight: 'bold',
        marginVertical: 5,
    },
});
