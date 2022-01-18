import React from 'react';
import { Entypo } from '@expo/vector-icons';
import { TouchableOpacity, StyleSheet, Text} from 'react-native';
import ImageModal from './ImageModal';

// The pop up modal that appears when you weant to add an image to you image library in the app
class AddGalleryModal extends React.Component {
    render() {
        //variables to keep track of the state of the image page, whether the addModal is open or closed ans so on
        const { isOpen, closeModal, takePhoto, selectFromCameraRoll } = this.props;
        return (
            <ImageModal style={styles.ImageModal} isOpen={ isOpen } closeModal={ closeModal }>
                <TouchableOpacity style={styles.Icon} onPress={closeModal}>
                    <Text style={styles.CloseAddModal}>
                        X
                    </Text>
                </TouchableOpacity>

                <TouchableOpacity
                    onPress={ () => takePhoto() }>
                    <Entypo style={ styles.Icon } name="camera" />
                </TouchableOpacity>

                <TouchableOpacity
                    onPress={ () => selectFromCameraRoll() }>
                    <Entypo style={ styles.Icon } name="image" />
                </TouchableOpacity>
            </ImageModal>
        );
    }
}

export default AddGalleryModal;

const styles = StyleSheet.create({
    CloseAddModal:{
        alignItems: 'flex-start',
        fontSize: 30,
    },
    Icon: {
        fontSize: 60,
        marginBottom: 30
    },
    ImageModal: {
        backgroundColor: 'lightgreen',
        padding: 50,
    }
});
