import React from 'react';
import { Image, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { withNavigation } from 'react-navigation';
import { deleteSingleContactConfirmation, validateName } from '../../services/FileServices/ValidationServices';
import { deleteExistingContact } from '../../services/FileServices/ContactFileServices';
import { MakePhoneCall } from '../../services/PhoneCallService/PhoneCallService';
import GlobalStyles from '../../styles/GlobalStyles';

// The page rendered when accessing a single contacts details
class ContactDetailsView extends React.Component {
    constructor(props){
        super(props);
    }
    // Update the contact list and go back to the ContactListView -- the update function is connected to the ContactListView
    async loadUpdatesAndGoBack () {
        await this.props.navigation.state.params.loadContactUpdates();
        await this.props.navigation.goBack();
    }
    // Update the contact list -- the update function is connected to the ContactListView
    async loadUpdates () {
        await this.props.navigation.state.params.loadContactUpdates();
    }
    // render the page
    render () {
        // The variables used to display the correct contact
        const contactName = this.props.navigation.state.params.contactName;
        const contactPhoneNumber = this.props.navigation.state.params.contactPhoneNumber;
        const contactPhoto = this.props.navigation.state.params.contactPhoto;
        const contactUUID = this.props.navigation.state.params.contactUUID;
        const contactColor = this.props.navigation.state.params.contactColor;
        const uniquePhoneNumbers = this.props.navigation.state.params.uniquePhoneNumbers;
        // Fetch the file name for deleting and recreating the file
        const FileName = validateName(contactName) + '-' + contactUUID + '.json';

        return (
            <View key={contactUUID} style={[GlobalStyles.Container, {backgroundColor: contactColor}]}>
                <Text style={GlobalStyles.HeaderText}>
                    Contact Details
                </Text>
                <View style={styles.ContactInfo}>
                    <Image source={{uri: contactPhoto}} style={styles.ContactImage}/>

                    <Text style={styles.ContactText}>
                        {contactName}
                    </Text>

                    <Text style={styles.ContactText}>
                        {contactPhoneNumber}
                    </Text>
                </View>

                <TouchableOpacity style={[GlobalStyles.Button]} onPress={() => {MakePhoneCall(contactPhoneNumber)}}>
                    <Text style={GlobalStyles.ButtonText}>
                        Call
                    </Text>
                </TouchableOpacity>

                <TouchableOpacity style={[GlobalStyles.Button]} onPress={() => {this.props.navigation.navigate('ModifyContactView', {contactName: contactName, contactPhoneNumber: contactPhoneNumber, contactPhoto : contactPhoto, contactUUID: contactUUID, contactColor: contactColor, loadContactUpdates: this.loadUpdates.bind(this), uniquePhoneNumbers: uniquePhoneNumbers})}}>
                    <Text style={GlobalStyles.ButtonText}>
                        Modify Information
                    </Text>
                </TouchableOpacity>

                <TouchableOpacity style={[GlobalStyles.Button]} onPress={() => {deleteSingleContactConfirmation(FileName, deleteExistingContact, this.loadUpdatesAndGoBack.bind(this))}}>
                    <Text style={GlobalStyles.ButtonText}>
                        Delete Contact
                    </Text>
                </TouchableOpacity>
            </View>
        );
    }
}

export default withNavigation(ContactDetailsView);

const styles = StyleSheet.create({
    ContactImage: {
        borderRadius: 115,
        height: 220,
        marginBottom: '5%',
        marginHorizontal: 30,
        width: 220,
    },
    ContactInfo: {
        alignItems: 'center',
        marginVertical: '10%',
    },
    ContactText: {
      fontSize: 30,
      fontWeight: 'bold',
      textAlign: 'center',
    },
})
