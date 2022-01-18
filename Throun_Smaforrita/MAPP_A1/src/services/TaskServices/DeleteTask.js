import React from 'react';
import * as FileSystem from 'expo-file-system';
import data from '../../resources/data.json';


async function deleteTask (TaskId, ListId, ListName, props) {
    data.tasks.map((task, index) => {
        if (task.id == TaskId) {
            data.tasks.splice(index,1);
            FileSystem.writeAsStringAsync(FileSystem.documentDirectory + 'data.json', JSON.stringify(data));
        }
        props.navigation.navigate('ListView', ListId, ListName, props);
    });
}

export default deleteTask;
