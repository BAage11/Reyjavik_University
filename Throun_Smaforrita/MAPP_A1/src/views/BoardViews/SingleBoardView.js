import React from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, ScrollView, TouchableOpacity, Alert} from 'react-native';
import { withNavigation } from 'react-navigation';
import data from '../../resources/data.json';
import deleteBoard from '../../services/BoardServices/DeleteBoard';
import GlobalStyles from '../../styles/GlobalStyles';

// function for popping up un alert for conformation about deleting the board
const deleteConformation = (Id, name, props) => {
    Alert.alert(
        'Do you want to delete the board:',
        name + '?',
        [
            {text: 'Yes', onPress: () => {deleteBoard(Id, props)}},
            {text: 'No', style: 'cancel'},
        ],
        {
            cancelable: true
        }
    );
}

// The returned page when entering a single board
const SingleBoardView = (props) => {
  // variables for keeping track of the board elements
  var BoardId;
  var BoardName;
  var ThumbnailPhoto;
    return (
        <View style={GlobalStyles.container}>
            <View style={styles.BoardTitle}>
                { data.boards.map((board) => {
                    if (board.id == props.navigation.state.params[0]) {
                        BoardId = board.id;
                        BoardName = board.name;
                        ThumbnailPhoto = board.thumbnailPhoto;
                        return (
                            <Text key={board.id}style={styles.BoardTitleText}>
                                {board.name}
                            </Text>
                        );
                    }
                })}
            </View>

            <View style={styles.ListItems}>
                <ScrollView>
                    {data.lists.map((list) => {
                        if (list.boardId == props.navigation.state.params[0]) {
                            return (
                                <TouchableOpacity key={list.id} style={[styles.ListItem, {backgroundColor: list.color }]} onPress={() => props.navigation.navigate('ListView', [list.id, list.name, props.navigation.state.params[0],props.navigation.state.params[1], props.navigation.state.params[2]])}>
                                    <Text style={styles.ListNameText}>
                                        {list.name}
                                    </Text>
                                </TouchableOpacity>
                            );
                        }
                    })}
                </ScrollView>
            </View>

            <Text style={styles.BoardHeader}>
                Actions
            </Text>

            <TouchableOpacity style={GlobalStyles.ActionButton} onPress={() => props.navigation.navigate('AddNewListView', [props.navigation.state.params[0], props.navigation.state.params[1]])}>
                <Text style={GlobalStyles.ButtonText}>
                    Create new list
                </Text>
            </TouchableOpacity>

            <TouchableOpacity style={GlobalStyles.ActionButton} onPress={() => props.navigation.navigate('ModifyBoardView', [props.navigation.state.params[0], props.navigation.state.params[1], props.navigation.state.params[2]])}>
                <Text style={GlobalStyles.ButtonText}>
                    Modify Board
                </Text>
            </TouchableOpacity>

            <TouchableOpacity style={GlobalStyles.ActionButton} onPress={() => {deleteConformation(BoardId, BoardName, props)}}>
                <Text style={GlobalStyles.ButtonText}>
                    Delete Board
                </Text>
            </TouchableOpacity>
        <StatusBar style='auto' />
        </View>
    );
  };

export default withNavigation(SingleBoardView);

const styles = StyleSheet.create({
    BoardHeader: {
        color: '#ffffff',
        fontSize: 20,
        fontStyle: 'italic',
        fontWeight: 'bold',
        marginVertical: 16,
    },
    BoardTitle: {
        flex: 2,
    },
    BoardTitleText: {
        fontSize: 30,
        fontStyle: 'italic',
        fontWeight: 'bold',
        marginVertical: 20,
    },
    ListItem: {
        alignItems: 'center',
        borderWidth: 3,
        height: 60,
        marginVertical: 10,
        width: 300,
    },
    ListItems: {
        flex: 7,
    },
    ListNameText: {
        fontSize: 18,
        fontWeight: 'bold',
        height: 60,
        marginVertical: 14,
        textAlign: 'center',
    },
    ListTitle: {
        flex: 3
    },
});
