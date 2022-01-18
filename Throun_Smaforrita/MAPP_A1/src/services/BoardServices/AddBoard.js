import React, { useState } from 'react';
import { Alert, Vibration } from 'react-native';
import { withNavigation } from 'react-navigation';
import * as FileSystem from 'expo-file-system';
import data from '../../resources/data.json';


const VIBE_SEC = 1000;

// If every field was filled in, update the board. 
// Else, vibrate and exit to board list view.
async function addBoard (BoardName, BoardPhoto, AllInputsFilledIn, props) {
    if (AllInputsFilledIn) {
        // Assigning an ID to the new board and make sure it's unique
        var NewBoardId = 1;
        if( data.boards.length > 0) {
            const HighestBoardId = data.boards[data.boards.length - 1].id;
            NewBoardId = HighestBoardId + 1;
        }
        // The new board object
        var NewBoardObject = {
            id: NewBoardId,
            name: BoardName,
            thumbnailPhoto: BoardPhoto
        };
        // Push the new board into the file system
        data.boards.push(NewBoardObject);
        await FileSystem.writeAsStringAsync(FileSystem.documentDirectory + 'data.json', JSON.stringify(data));
    }
    // Vibrate if something went wrong
    else{
        Vibration.vibrate(VIBE_SEC, false);
        Alert.alert("Missing input field(s).\nPlease try again.")
    }
}

export default addBoard;
