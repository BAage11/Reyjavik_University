import React from 'react';
import { View, Text, StyleSheet, Dimensions } from 'react-native';
import NativeModal from 'react-native-modal';

// for the AddGalleryModal which is a pop up window in the BoardGalleryView
const ImageModal = ({ isOpen, closeModal, title, children }) => (
    <NativeModal isVisible={ isOpen } hasBackdrop={ true } onBackButtonPress={ closeModal } onSwipeComplete={ closeModal } swipeDirection={[ "up", "down" ]} style={ styles.Modal }>
        <View style={ styles.Body }>
            <Text>{ title }</Text>
            { children }
        </View>
    </NativeModal>
);

export default ImageModal;

const { width: winWidth } = Dimensions.get('window');

const styles = StyleSheet.create({
    Body: {
        alignItems: 'center',
        backgroundColor: 'white',
        borderRadius: 10,
        flex: 1,
        flexGrow: .3,
        justifyContent: 'center',
        padding: 40,
        width: winWidth - 100,
    },
    Modal: {
        alignItems: 'center',
        flex: 1,
        justifyContent: 'center',
    },
});
