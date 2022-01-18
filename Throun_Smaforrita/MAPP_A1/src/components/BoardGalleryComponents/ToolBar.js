import React from 'react';
import { colors } from '../../styles/GlobalStyles';
import { View, TouchableHighlight, Text, StyleSheet} from 'react-native';

// the toolbar at the top of BoardGalleryView where you have the option to add / delete images
const Toolbar = ({ hasSelectedImages, onAdd, onRemove }) => (
    <View styleName="horizontal" style={ styles.Toolbar }>
        <TouchableHighlight style={ styles.ToolbarAction } onPress={ onAdd }>
            <Text style={ styles.ToolbarActionText }>
                Add image
            </Text>
        </TouchableHighlight>

        <TouchableHighlight style={ styles.ToolbarAction } onPress={ onRemove } disabled={ !hasSelectedImages }>
            <Text style={ [ styles.ToolbarActionText, !hasSelectedImages ? { color: 'grey' } : {} ] }>
                Delete
            </Text>
        </TouchableHighlight>
    </View>
);

export default Toolbar;

const styles = StyleSheet.create({
    Toolbar: {
        alignItems: 'center',
        backgroundColor: colors.jordyBlue,
        flexDirection: 'row',
        height: 80,
        justifyContent: 'center',
    },
    ToolbarAction: {
        alignItems: 'center',
        flex: 1,
    },
    ToolbarActionText: {
        color: 'black',
        fontSize: 16,
        fontWeight: 'bold',
    },
});
