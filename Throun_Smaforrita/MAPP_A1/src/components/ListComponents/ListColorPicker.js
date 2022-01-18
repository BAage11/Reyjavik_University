import React from 'react'
import {colorList} from '../../styles/GlobalStyles';
import { StyleSheet, Text, ScrollView, TouchableOpacity, TextInput, Alert } from 'react-native';
import modifyColorList from '../../services/ListServices/ModifyColorList';

// this is a scrollview component inside the ModifyListColorView
// where a user is able to tap on a color to change the lsits color
const ListColorPicker = (props) => {
    return(
        <ScrollView style={styles.ColorPicker}>
            {colorList.map((color) => {
                return(
                    <TouchableOpacity key={color} style={[styles.ColorItem, {backgroundColor: color}]} onPress={() => {
                        modifyColorList(props.listId, color, props, props.boardId, props.boardName, props.thumbnail);
                        props.props.navigation.navigate('SingleBoardView', [props.boardId, props.boardName, props.thumbnail, props])}}>

                        <Text style={styles.ColorItemText}>
                            Tap to choose this color
                        </Text>
                    </TouchableOpacity>
                );
            })}
        </ScrollView>
    )
}

export default ListColorPicker

const styles = StyleSheet.create({
    ColorPicker: {
        marginVertical: 50,
        width: 300,
    },
    ColorItem: {
        alignItems: 'center',
        height: 50,
        marginVertical: 5,
        padding: 10,
    },
    ColorItemText: {
        fontSize: 16,
        fontWeight: 'bold',
    },
})
