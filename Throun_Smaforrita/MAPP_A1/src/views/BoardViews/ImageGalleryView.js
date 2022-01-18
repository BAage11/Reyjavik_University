import React from 'react';
import {colors} from '../../styles/GlobalStyles/';
import { getAllImages, addImage, remove } from '../../services/BoardGalleryServices/FileServices';
import { headings } from '../../styles/GlobalStyles';
import { takePhoto, selectFromCameraRoll } from '../../services/BoardGalleryServices/ImageServices';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import AddGalleryModal from '../../components/BoardGalleryComponents/AddGalleryModal';
import GalleryList from '../../components/BoardGalleryComponents/GalleryList';
import Spinner from '../../components/BoardGalleryComponents/Spinner';
import Toolbar from '../../components/BoardGalleryComponents/ToolBar';

// the page rendered when wanting to view the imgage gallery
class ImageGalleryView extends React.Component {
    static navigationOptions = {
        title: 'Gallery'
    }
    // keeping track o fthe state of all images and the add modal
    state = {
        // All images within the application directory
        images: [],
        // All selected images
        selectedImages: [],
        // A boolean flag to indicate whether the images are being loaded or not
        loadingImages: true,
        // A boolean flag to indicate whether the modal to add an image is open or not
        isAddModalOpen: false
    }
    // fetching all images
    async componentDidMount() {
        await this._fetchItems();
    }
    // fetching all images

    async _fetchItems() {
        this.setState({ loadingImages: true });
        const images = await getAllImages();
        this.setState({ loadingImages: false, images });
    }
    // select the image on long press
    onImageLongPress(name) {
        const { selectedImages } = this.state;
        if (selectedImages.indexOf(name) !== -1) {
            // The image is already within the list
            this.setState({ selectedImages: selectedImages.filter(image => image !== name) });
        } else {
            // Add the new image
            this.setState({ selectedImages: [ ...selectedImages, name ] });
        }
    }
    // delete the selected images
    async deleteSelectedImages() {
        const { selectedImages, images } = this.state;
        this.setState({ loadingImages: true })
        await Promise.all(selectedImages.map(image => remove(image)));
        this.setState({
            selectedImages: [],
            // Only retrieve images which were NOT part of the selected images list
            images: images.filter(image => selectedImages.indexOf(image.name) === -1),
            loadingImages: false
        });
    }
    // take a photo and add it to the gallery
    async takePhoto() {
        const photo = await takePhoto();
        if (photo.length > 0) { await this.addImage(photo); }
    }
    // pick a photo from the camera roll and add it to the gallery
    async selectFromCameraRoll() {
        const photo = await selectFromCameraRoll();
        if (photo.length > 0) { await this.addImage(photo); }
    }
    // add an image to the gallery
    async addImage(image) {
        this.setState({ loadingImages: true });

        const newImage = await addImage(image);
        const { images } = this.state;
        this.setState({ images: [ ...images, newImage ], loadingImages: false, isAddModalOpen: false });
    }
    // for displaying the image caption
    displayCaption() {
        const { selectedImages } = this.state;
        if (selectedImages.length === 0) { return; }

        let itemCaption = 'images';
        if (selectedImages.length === 1) {
            itemCaption = 'image';
        }
        return <Text style={ [ headings.h3, { marginLeft: 20, marginTop: 10, marginBottom: 5 } ] }>{ selectedImages.length } { itemCaption } selected</Text>;
    }
    // rendering the view
    render() {
        const { selectedImages, loadingImages, images, isAddModalOpen } = this.state;
        return (
            <View style={{ flex: 1 }}>
                <Toolbar
                    hasSelectedImages={ selectedImages.length > 0 }
                    onAdd={ () => this.setState({ isAddModalOpen: true }) }
                    onRemove={ () => this.deleteSelectedImages() } />
                <Text>
                    Press and hold images if you want to select them for deletion
                </Text>
                {
                    loadingImages
                    ?
                    <Spinner />
                    :
                    <>
                        { this.displayCaption() }
                        <GalleryList
                            images={ images }
                            selectedImages={ selectedImages }
                            onLongPress={ name => this.onImageLongPress(name) } />
                    </>
                }
                <AddGalleryModal
                    isOpen={ isAddModalOpen }
                    closeModal={ () => this.setState({ isAddModalOpen: false }) }
                    takePhoto={ () => this.takePhoto() }
                    selectFromCameraRoll={ () => this.selectFromCameraRoll() }>
                </AddGalleryModal>
            </View>
        );
    }
}

export default ImageGalleryView;

const styles = StyleSheet.create({
    CloseAddModal:{
        color: colors.jordyBlue,
        height: 10,
        width: 10,
    },
})
