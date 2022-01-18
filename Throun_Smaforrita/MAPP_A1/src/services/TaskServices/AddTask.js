import React, { useState } from 'react';
import { Vibration } from 'react-native';
import * as FileSystem from 'expo-file-system';
import data from '../../resources/data.json';


const VIBE_SEC = 1000;

// If every field was filled in, update the task.
// Else, vibrate and exit to task list view.
async function addTask (TaskName, TaskDescription, TheListId, AllInputsFilledIn) {
    if (AllInputsFilledIn){
        // create new id for the new task, and make sure it is nunique
        var NewTaskId = 1;
        // if the task list is empty the id will be 1, else we find the last id and increment by 1
        if( data.tasks.length > 0) {
            const HighestTaskId = data.tasks[data.tasks.length - 1].id;
            NewTaskId = HighestTaskId + 1;
        }
        // create the new task object to push into the file system
        var NewTaskObject = {
            id: NewTaskId,
            name: TaskName,
            description: TaskDescription,
            isFinished: false,
            listId: TheListId
        };
        // add the new task to the file system
        data.tasks.push(NewTaskObject);
        FileSystem.writeAsStringAsync(FileSystem.documentDirectory + 'data.json', JSON.stringify(data));
    } else{
        Vibration.vibrate(VIBE_SEC, false);
    }
}

export default addTask;
