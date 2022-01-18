import React, { useState } from 'react';
import { Vibration } from 'react-native';
import * as FileSystem from 'expo-file-system';
import data from '../../resources/data.json';

// variable for vibration duration
const VIBE_SEC = 1000;
// a funciton for modifying a board (name/photo)
async function modifyBoard (BoardId, BoardName, BoardPhotoUrl, props, AllInputsFilledIn) {
    if (AllInputsFilledIn){
        data.boards.map((board) => {
            if (board.id == BoardId) {
                board.name = BoardName;
                board.thumbnailPhoto = BoardPhotoUrl;
                FileSystem.writeAsStringAsync(FileSystem.documentDirectory + 'data.json', JSON.stringify(board));
            }
        });
    } else{
        Vibration.vibrate(VIBE_SEC);
    }
}

export default modifyBoard;
