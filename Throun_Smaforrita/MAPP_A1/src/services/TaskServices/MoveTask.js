import React from 'react';
import * as FileSystem from 'expo-file-system';
import data from '../../resources/data.json';


async function MoveTask (TaskId, ListId, props){
    data.tasks.map((task) => {
        if (task.id == TaskId) {
            task.listId = ListId
            FileSystem.writeAsStringAsync(FileSystem.documentDirectory + 'data.json', JSON.stringify(data));
            props.navigation.navigate('ListView', props);
        }
    });
};

export default MoveTask;
