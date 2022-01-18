import React, { useState } from 'react';
import * as FileSystem from 'expo-file-system';
import data from '../../resources/data.json';

// a function for modifying the color of a list
async function modifyColorList (ListId, ListColor, props, BoardId, BoardName, BoardThumbnailPhoto) {
    data.lists.map((list) => {
        if (list.id == ListId) {
            list.color = ListColor;
            FileSystem.writeAsStringAsync(FileSystem.documentDirectory + 'data.json', JSON.stringify(data));
        }
    });
}

export default modifyColorList;
