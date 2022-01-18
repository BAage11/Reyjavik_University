import React, { useState } from 'react';
import { Vibration } from 'react-native';
import * as FileSystem from 'expo-file-system';
import data from '../../resources/data.json';


const VIBE_SEC = 1000;

// If every field was filled in, add the new item to the file system.
// Else, vibrate and exit to list view.
async function addList (ListName, TheBoardId, NameFilledIn) {
    // create a new id for the new list
    var NewListId = 1;
    if (NameFilledIn){
      // if the list list is empty the id will be 1 else we find the last lsit id and increment it by 1
        if( data.lists.length > 0) {
            const HeighestListId = data.lists[data.lists.length - 1].id;
            NewListId = HeighestListId + 1;
        }
        // creating the new lsit object
        var NewListObject = {
            id: NewListId,
            name: ListName,
            color: '#ffffff',
            boardId: TheBoardId
        };
        // pushing the new list object into the file system
        data.lists.push(NewListObject);
        await FileSystem.writeAsStringAsync(FileSystem.documentDirectory + 'data.json', JSON.stringify(data));
    } else{
        Vibration.vibrate(VIBE_SEC, false);
    }
}

export default addList;
