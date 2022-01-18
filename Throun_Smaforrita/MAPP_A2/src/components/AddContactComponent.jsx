import React from 'react';
import Modal from 'react-native-modal';
import { Image, StyleSheet, Text, TextInput, TouchableOpacity, ScrollView, View, KeyboardAvoidingView, Keyboard, TouchableWithoutFeedback} from 'react-native';
import 'react-native-get-random-values';
import { v4 as uuidV4 } from 'uuid';
import { withNavigation } from 'react-navigation';
import { cleanPhoneNumber, inputIsMissingAddContact } from '../services/FileServices/ValidationServices'
import { createNewContact } from '../services/FileServices/ContactFileServices'
import { getImageByCamera } from '../services/ImageServices/TakePhotoService';
import { getImageFromCameraRoll } from '../services/ImageServices/AddFromCameraRollService';
import AddImageComponent from './AddImageComponent';
import ColorPickerComponent from './ColorPickerComponenent'
import GlobalStyles, {colors} from '../styles/GlobalStyles';


// The component used in AddContactView, used for entering in a new contacts name, phone, and photo and creating the contact
class AddContactComponent extends React.Component {
    constructor(props){
        super(props);
        // Variables to keep trac of to display changes dinamically
        this.state = {
            contactName: '',
            contactPhoneNumber: '',
            contactPhoto: 'https://www.techpowerusa.com/wp-content/uploads/2017/06/default-user.png',
            contactColor: '#eeeeee',
            isColorPickerOpen: false,
            currentErrorMessage: '',
        }
        this.isValid = false;
    };
    // Function vor resetting all the state variables so that they are initially empty every time a contact is added
    resetValues() {
        this.setState({contactName: '', contactPhoneNumber: '', contactPhoto: 'https://www.techpowerusa.com/wp-content/uploads/2017/06/default-user.png' })
    }

    // Validation of all elements being filled in and alert user what is wrong if something is missing
    inputValidation() {
        // Check whether all text inputs are filled in
        if (this.state.contactName && this.state.contactPhoneNumber) {
            // Check if the phone number is a valid number
            if (!isNaN(this.state.contactPhoneNumber)) {
                // Check if the phone number is at lease 7 digits
                if ( this.state.contactPhoneNumber.length >= 7) {
                    // Check if the phone number entered already exists
                    if (!this.props.navigation.state.params.uniquePhoneNumbers.includes(this.state.contactPhoneNumber)) {
                        // Fetching a UUID for the contact file
                        const UUID = uuidV4();
                        // Creating the new contact file for the modified contact
                        const NewContactObject = {
                            'contactName': this.state.contactName,
                            'contactPhoneNumber': cleanPhoneNumber(this.state.contactPhoneNumber),
                            'contactPhoto': this.state.contactPhoto,
                            'contactUUID': UUID,
                            'contactColor': this.state.contactColor,
                        }
                        createNewContact(NewContactObject);
                        // remove any error message
                        this.setState({currentErrorMessage: ''});
                        // Accept the input as valid
                        this.isValid = true;
                    } else {
                        // Update the error message
                        this.setState({currentErrorMessage: 'This phone number is registered to someone else'});
                        this.isValid = false;
                    }
                } else {
                    // Update the error message
                    this.setState({currentErrorMessage: 'Phone number must be at least 7 digits'});
                    this.isValid = false;
                }
            } else {
                // Update the error message
                this.setState({currentErrorMessage: 'Phone number must be a valid number'});
                this.isValid = false;
            }
        }
        // Check if only contact name is filled in
        else if (this.state.contactName){
            this.setState({currentErrorMessage: 'You need to enter a phone number'});
            this.isValid = false;
        }
        // Check if only contact phone number is filled in
        else if (this.state.contactPhone){
            this.setState({currentErrorMessage: 'You need to enter the contacts name'});
            this.isValid = false;
        }
        // All inputs are empty
        else {
            this.setState({currentErrorMessage: 'You need to enter the contacts name and phone number'});
            this.isValid = false;
        }
    }

    // Add photo to contact via camera roll
    async cameraRollUpload() {
        const NewPhoto = await getImageFromCameraRoll();
        this.setState({contactPhoto: NewPhoto})
    }

    // Add photo to contact via taking a photo
    async cameraUpload () {
        const NewPhoto = await getImageByCamera();
        this.setState({contactPhoto: NewPhoto});
    }
    // Load updates to the contact list and navigate back to the contact list view
    async loadUpdatesAndGoBack () {
        await this.props.navigation.state.params.loadContactUpdates();
        this.props.navigation.goBack();
        this.resetValues();
    }
    // Close the color picker modal
    async closeColorPicker() {
        this.setState({isColorPickerOpen: false})
    }
    // Open the color picker modal
    async openColorPicker() {
        this.setState({isColorPickerOpen: true})
    }
    // Update the contacts color theme after a color is chosen
    async changeColor(newColor) {
        this.setState({contactColor: newColor});
    }
    // Render the component
    render() {
        // get the state variables to display inside the view
		const { contactName, contactPhoneNumber, contactPhoto, contactColor } = this.state;
        return (
            <KeyboardAvoidingView style={[GlobalStyles.Container, {backgroundColor: contactColor}]} behavior={Platform.OS == "ios" ? "padding" : "height"} keyboardVerticalOffset={100}>
                <TouchableWithoutFeedback onPress={Keyboard.dismiss}>
                    <ScrollView>
                        <View style={[GlobalStyles.Container, {backgroundColor: contactColor}]}>
                            <Modal isVisible={this.state.isColorPickerOpen} animationIn='slideInDown' animationOut='slideOutUp' animationInTiming={500} animationOutTiming={500}>
                                <View style={styles.ListColorPicker}>
                                    <ColorPickerComponent closeColorPicker={this.closeColorPicker.bind(this)} changeColor={this.changeColor.bind(this)}>
                                    </ColorPickerComponent>
                                </View>
                            </Modal>
                            <Text style={[styles.HeaderTextStyle, {backgroundColor: contactColor}]}>
            					Add New Contact
            				</Text>

            				<View>
            					<Image source={{ uri: contactPhoto }} style={styles.ContactImage}/>

                                <AddImageComponent cameraUpload={this.cameraUpload.bind(this)} cameraRollUpload={this.cameraRollUpload.bind(this)}/>
            				</View>

                            <Text style={[GlobalStyles.NormalText, {marginRight: 200, fontWeight: 'bold', fontStyle: 'italic', fontSize: 18}]}>
                                Enter contact name
                            </Text>

            				<TextInput
                                autoCompleteType='off'
                                autoCorrect={false}
            					style={GlobalStyles.TextInput}
                                placeholderTextColor='grey'
            					onChangeText={(contactName) => this.setState({ contactName })}
            					value={contactName}
            					maxLength={30}
                                returnKeyType='done'
            					placeholder={'Contact name'}
                            />

                            <Text style={[GlobalStyles.NormalText, {marginRight: 120, fontWeight: 'bold', fontStyle: 'italic', fontSize: 18}]}>
                                Enter contact phone number
                            </Text>

            				<TextInput
                                autoCompleteType='off'
                                autoCorrect={false}
            					style={GlobalStyles.TextInput}
                                placeholderTextColor='grey'
            					onChangeText={(contactPhoneNumber) => this.setState({ contactPhoneNumber })}
            					value={contactPhoneNumber}
            					keyboardType='numeric'
                                returnKeyType='done'
            					placeholder={'Contact phone nr.'}
                            />

                            <TouchableOpacity style={GlobalStyles.Button} onPress={async () => {await this.openColorPicker()}}>
                                <Text style={GlobalStyles.ButtonText}>
                                    Add color theme
                                </Text>
                            </TouchableOpacity>

                            <TouchableOpacity style={GlobalStyles.Button} onPress={async () => {await this.inputValidation(); this.isValid ? await this.loadUpdatesAndGoBack() : await inputIsMissingAddContact(this.state.currentErrorMessage)}}>
                                <Text style={GlobalStyles.ButtonText}>
                                    Save contact
                                </Text>
                            </TouchableOpacity>
                        </View>
                    </ScrollView>
                </TouchableWithoutFeedback>
            </KeyboardAvoidingView>
        );
    }
}

export default withNavigation(AddContactComponent);

const styles = StyleSheet.create({
	ContactImage: {
        alignSelf: 'center',
		borderWidth: 3,
		borderRadius: 115,
		height: 150,
		marginTop: 10,
		width: 150,
    },
    HeaderTextStyle: {
        backgroundColor: colors.freshAir,
        color: '#000000',
        fontSize: 28,
        fontWeight: 'bold',
        height: 60,
        marginBottom: 5,
        paddingTop: 10,
        textAlign: 'center',
        width: '100%',
    },
    ListColorPicker: {
		flex: 1,
		justifyContent: 'center',
		alignItems: 'center'

	},
});
