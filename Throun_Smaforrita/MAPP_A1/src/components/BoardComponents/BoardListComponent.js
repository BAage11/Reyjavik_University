import React from 'react';
import { StyleSheet, Text, View, TouchableOpacity, Image } from 'react-native';
import { withNavigation } from 'react-navigation';

// this is a component used for the BoardListView where each board is made of the component
const BoardListComponent = (props) => {
    return (
            <TouchableOpacity style={styles.BoardItem} onPress={() => props.navigation.navigate('SingleBoardView', [props.id, props.name, props.thumbnailPhoto])}>
                <Text style={styles.BoardItemHeader}>
                    {props.name}
                </Text>

                <Image style={styles.Image}
                    style={styles.ThumbnailPhoto}
                    source={{uri: props.thumbnailPhoto}}
                />
            </TouchableOpacity>
      )
};

export default withNavigation(BoardListComponent);

const styles = StyleSheet.create({
    BoardItem: {
        alignItems: 'flex-start',
        backgroundColor: '#42638E',
        height: 80,
        marginVertical: 10,
        width: 300,

    },
    BoardItemHeader: {
        color: '#ffffff',
        fontSize: 18,
        fontWeight: 'bold',
        position: "relative",
    },
    Image:{
        borderWidth: 2,
    },
    ThumbnailPhoto: {
        borderColor: '#000000',
        borderWidth: 2,
        flex: 3,
        height: '100%',
        width: '100%',
    }

});
