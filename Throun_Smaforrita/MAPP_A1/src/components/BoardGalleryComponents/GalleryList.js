import React from 'react';
import { View, FlatList, StyleSheet } from 'react-native';
import ImageThumbnail from './ImageThumbnail';

// the list of images rendered on the BoardGalleryView page takes in a list of images and a function to use onlongpress
const GalleryList = ({ images, selectedImages, onLongPress }) => (
    <View style={ styles.ListContainer }>
        <FlatList numColumns={ 3 } data={ images } extraData={ selectedImages }
            renderItem={ ({ item: { file, name } }) => {
                return (
                    <ImageThumbnail isSelected={ selectedImages.indexOf(name) !== -1 } onLongPress={ onLongPress } name={ name } file={ file } />
                );
            }}
            keyExtractor={ image => image.name } />
    </View>
);

export default GalleryList;

const styles = StyleSheet.create({
    ListContainer: {
        flex: 1
    }
});
