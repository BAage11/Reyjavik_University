import React from 'react';
import * as FileSystem from 'expo-file-system';
import data from '../../resources/data.json';

// a function for deleting a list from the file system
async function deleteList (Id, props) {
    data.lists.map((list, index) => {
        if (list.id == Id) {
            data.lists.splice(index,1);
            data.tasks.map((task, index) => {
                if (task.listId == Id) {
                    data.tasks.splice(index,1);
                }
            });
        }
    });
   FileSystem.writeAsStringAsync(FileSystem.documentDirectory + 'data.json', JSON.stringify(data));
   props.navigation.navigate('SingleBoardView', props)
}

export default deleteList;
