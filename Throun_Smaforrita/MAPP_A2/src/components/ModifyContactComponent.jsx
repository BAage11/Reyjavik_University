import React from 'react';
import Modal from 'react-native-modal';
import { Image, StyleSheet, Text, TextInput, TouchableOpacity, ScrollView, KeyboardAvoidingView, Keyboard, TouchableWithoutFeedback, View } from 'react-native';
import { withNavigation } from 'react-navigation';
import { createNewContact, deleteExistingContact } from '../services/FileServices/ContactFileServices'
import { getImageByCamera } from '../services/ImageServices/TakePhotoService';
import { getImageFromCameraRoll } from '../services/ImageServices/AddFromCameraRollService';
import { inputIsMissingAddContact, validateName } from '../services/FileServices/ValidationServices'
import AddImageComponent from './AddImageComponent';
import ColorPickerComponent from './ColorPickerComponenent'
import GlobalStyles, { colors } from '../styles/GlobalStyles';

// The component for modifying an existing contact
class ModifyContactComponent extends React.Component {
    constructor(props){
        super(props);
        // Keep track if all important contact variables.
        // Initialize them with the parameters passed on from the ModifyContactView
        this.state = {
            contactName: this.props.navigation.state.params.contactName,
            contactPhoneNumber: this.props.navigation.state.params.contactPhoneNumber,
            contactPhoto: this.props.navigation.state.params.contactPhoto,
            contactColor: this.props.navigation.state.params.contactColor,
            currentErrorMessage: '',
            isColorPickerOpen: false,
        }
        this.isValid = true;
    };

    // Validation of all elements being filled in
    inputValidation() {
        // Check whether all text inputs are filled in
        if (this.state.contactName && this.state.contactPhoneNumber && this.state.contactPhoto) {
            // Check if the phone number is a valid number
            if (!isNaN(this.state.contactPhoneNumber)) {
                // Check if the phone number is at lease 7 digits
                if ( this.state.contactPhoneNumber.length >= 7) {
                    // Check if the phone number entered already exists
                    if (this.props.uniquePhoneNumbers && (!this.props.uniquePhoneNumbers.includes(this.state.contactPhoneNumber) || (this.state.contactPhoneNumber === this.props.navigation.state.params.contactPhoneNumber))) {
                        // Delete the contacts current file before recreating it
                        const FileName = validateName(this.props.navigation.state.params.contactName) + '-' + this.props.navigation.state.params.contactUUID + '.json';
                        deleteExistingContact(FileName);
                        // Creating the new updated contact object with the state variables, UUID stays the same
                        const NewContactObject = {
                            'contactName': this.state.contactName,
                            'contactPhoneNumber': this.state.contactPhoneNumber,
                            'contactPhoto': this.state.contactPhoto,
                            'contactUUID': this.props.contactUUID,
                            'contactColor': this.state.contactColor,
                        }
                        // Creating the new contact file for the modified contact
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
                this.setState({currentErrorMessage: 'Invalid phone number (only digits allowed)'});
                this.isValid = false;
            }
        } else {
            // Update the error message
            this.setState({currentErrorMessage: 'All input fields must be filled in'});
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
    // Update the contact list and navigate back tot he contact list view -- connected to the function
    async loadUpdatesAndGoBack () {
        await this.props.navigation.state.params.loadContactUpdates();
        this.props.navigation.navigate('ContactListView');
    }
    // Close the color picker model
    async closeColorPicker() {
        this.setState({isColorPickerOpen: false})
    }
    // Open the color picker model
    async openColorPicker() {
        this.setState({isColorPickerOpen: true})
    }
    // Update the color associated with each user
    async changeColor(newColor) {
        this.setState({contactColor: newColor});
    }
    // reqender the component
    render() {
        // Fetch the state variables for displaying the contact correctly
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

                            <Text style={[GlobalStyles.HeaderText, {backgroundColor: this.state.contactColor}]}>
            					Modify contact details
            				</Text>

            				<View>
            					<Image source={{ uri: contactPhoto }} style={styles.ContactImage}/>

                                <AddImageComponent cameraUpload={this.cameraUpload.bind(this)} cameraRollUpload={this.cameraRollUpload.bind(this)}/>

                            </View>

                            <Text style={[GlobalStyles.NormalText, {marginRight: 200, fontWeight: 'bold', fontStyle: 'italic', fontSize: 18}]}>
                                Enter new name
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
                                Enter new phone number
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
                            >
            				</TextInput>
                            <TouchableOpacity style={GlobalStyles.Button} onPress={async () => {await this.openColorPicker()}}>
                                <Text style={GlobalStyles.ButtonText}>
                                    Change color scheme
                                </Text>
                            </TouchableOpacity>

                            <TouchableOpacity style={GlobalStyles.Button} onPress={async () => {await this.inputValidation(); this.isValid ? await this.loadUpdatesAndGoBack() : await inputIsMissingAddContact(this.state.currentErrorMessage)}}>
                                <Text style={GlobalStyles.ButtonText}>
                                    Save changes
                                </Text>
                            </TouchableOpacity>
                        </View>
                </ScrollView>
            </TouchableWithoutFeedback>
        </KeyboardAvoidingView>
        );
    }
}

export default withNavigation(ModifyContactComponent);

const styles = StyleSheet.create({
	ContactImage: {
		alignSelf: 'center',
		borderRadius: 115,
		borderWidth: 3,
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
