import React, { useState } from 'react';
import { Vibration } from 'react-native';
import * as FileSystem from 'expo-file-system';
import data from '../../resources/data.json';


const VIBE_SEC = 1000;
// a function for modifying a list that already exists by updating it's Name
// dont need all these parameters, will fix it if we have time
async function modifyList (ListId, ListName, props, BoardId, BoardName, BoardThumbnailPhoto, AllInputsFilledIn) {
    if (AllInputsFilledIn){
        data.lists.map((list) => {
            if (list.id == ListId) {
                list.name = ListName;
                FileSystem.writeAsStringAsync(FileSystem.documentDirectory + 'data.json', JSON.stringify(data));
            }
        });
    } else{
        Vibration.vibrate(VIBE_SEC, false);
    }
}

export default modifyList;
