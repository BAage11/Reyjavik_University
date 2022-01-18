import React, { useState } from 'react';
import { Vibration } from 'react-native';
import data from '../../resources/data.json';
import * as FileSystem from 'expo-file-system';


const VIBE_SEC = 1000;

async function modifyTask (TaskId, TaskName, TaskDescription, TheListId, TaskIsFinished, AllInputsFilledIn) {
    if (AllInputsFilledIn){
        data.tasks.map((task) => {
            if (task.id == TaskId) {
                task.name = TaskName;
                task.description = TaskDescription;
                task.isFinished = TaskIsFinished;
                //data.tasks.push(task);
            }
        });
        FileSystem.writeAsStringAsync(FileSystem.documentDirectory + 'data.json', JSON.stringify(data));
    } else {
        Vibration.vibrate(VIBE_SEC, false);
    }
}

export default modifyTask;
