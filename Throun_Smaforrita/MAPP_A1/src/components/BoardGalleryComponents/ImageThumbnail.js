import React from 'react';
import { AntDesign } from '@expo/vector-icons';
import { Image, View, TouchableOpacity, StyleSheet } from 'react-native';
import { withNavigation } from 'react-navigation';

// the component used for each image in the gallry list
const ImageThumbnail = ({ file, name, onLongPress, isSelected, navigation: { navigate } }) => (
    <TouchableOpacity onLongPress={ () => onLongPress(name) } onPress={ () => navigate('Preview', { fileName: name }) }>
        {isSelected ?
            <AntDesign name="checkcircleo" style={ styles.Checkmark } />
            :
            <></>
        }
        <View style={ { opacity: isSelected ? .5 : 1 } }>
            <Image style={ styles.GalleryImage } resizeMode="cover" source={{ uri: `data:image/jpeg;base64,${file}` }} />
        </View>
    </TouchableOpacity>
);

export default withNavigation(ImageThumbnail);

const styles = StyleSheet.create({
    GalleryImage: {
        width: 125,
        height: 120,
        margin: 6,
        borderWidth: 2,
    },
    Checkmark: {
        fontSize: 16,
        position: 'absolute',
        right: 15,
        top: 15,
    },
    Image: {
        height: 115,
        margin: 10,
        width: 115,
    },
});
