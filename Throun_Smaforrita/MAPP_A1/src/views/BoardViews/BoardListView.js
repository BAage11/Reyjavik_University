import React from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, ScrollView, Image, TouchableOpacity, Button, Header } from 'react-native';
import BoardListComponent from '../../components/BoardComponents/BoardListComponent';
import data from '../../resources/data.json';
import GlobalStyles from '../../styles/GlobalStyles';


const BoardListView = (props) => {
    return (
        <View style={GlobalStyles.container}>
            <Text style={styles.BoardHeader}>
                Your current boards
            </Text>

            <ScrollView style={styles.BoardList}>
                {data.boards.map((board) => {
                    return (
                        <View key={board.id} >
                            <BoardListComponent id={board.id} name={board.name} thumbnailPhoto={board.thumbnailPhoto}/>
                        </View>
                    );
                })}
            </ScrollView>

            <Text style={styles.BoardHeader2}>
                Actions
            </Text>

            <TouchableOpacity style={GlobalStyles.ActionButton} onPress={() => props.navigation.navigate('AddNewBoardView', props)}>
                <Text style={GlobalStyles.ButtonText}>
                    Add new board
                </Text>
            </TouchableOpacity>
            <TouchableOpacity style={GlobalStyles.ActionButton} onPress={() => {props.navigation.navigate('ImageGalleryView')}}>
                <Text style={GlobalStyles.ButtonText}>
                    Your images
                </Text>
            </TouchableOpacity>
        <StatusBar style='auto' />
        </View>
    );
};

export default BoardListView;

const styles = StyleSheet.create({
    BoardHeader: {
        fontSize: 30,
        fontStyle: 'italic',
        fontWeight: 'bold',
        marginVertical: 20,
    },
    BoardHeader2: {
        color: '#ffffff',
        fontSize: 22,
        fontStyle: 'italic',
        fontWeight: 'bold',
        marginVertical: 4,
    },
    BoardItem: {
        height: 100,
        top: 0,
        width: 300,
    },
    BoardList: {
        flex: 5,
    },
});
