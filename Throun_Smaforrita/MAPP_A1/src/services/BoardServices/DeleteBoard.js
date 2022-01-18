import React from 'react';
import * as FileSystem from 'expo-file-system';
import data from '../../resources/data.json';


// Function for deleting an existing board
async function deleteBoard (BoardId, props) {
    var BoardsToKeep = [];
    var ListsToKeep = [];
    var ListIds = [];
    var TasksToKeep = [];
    // filter out the boards which we are going to keep after the deletion
    data.boards.filter((board, index, arr) => {
        if (board.id != BoardId) {
            BoardsToKeep.push(board);
            }
    });
    // filter out the lists which we are going to keep after the deletion
    data.lists.filter((list, index, arr) => {
        if (list.boardId != BoardId) {
            ListsToKeep.push(list);
            ListIds.push(list.id);
        }
    });
    // filter out the tasks which we are going to keep after the deletion
    data.tasks.filter((task, index, arr) => {
        if (ListIds.includes(task.listId)) {
            TasksToKeep.push(task);
        }
    });
    // create the nbew data object where all items which were supposed to be deleted are not in
    data.boards = BoardsToKeep;
    data.lists = ListsToKeep;
    data.tasks = TasksToKeep;
    // write to the file system the changes in the data object
    FileSystem.writeAsStringAsync(FileSystem.documentDirectory + 'data.json', JSON.stringify(data));
    // navigate back to the board list view 
    props.navigation.navigate('BoardListView', props, data);
}

export default deleteBoard;
