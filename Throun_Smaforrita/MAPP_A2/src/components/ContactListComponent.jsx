import React from 'react';
import { Image, ScrollView, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { withNavigation } from 'react-navigation';
import GlobalStyles from '../styles/GlobalStyles';

// The component for displaying the contact list
class ContactListComponent extends React.Component {
    constructor(props) {
        super(props);
    };
    // Function for updating the contact list -- connected to the same function inside the ContactListView
    async loadContactUpdates() {
        await this.props.loadContactUpdates();
    }

    render() {
        // Fetch all the current contacts from the parameter passed on from the ContactListView
        const AllContacts = this.props.allContacts;
        // If AllContacts is not empty return a component with a list of all the contacts
        if (AllContacts) {
            return (
                <View style={styles.ContactList}>
                    <Text style={styles.ContactListHeader}>
                        Your Contacts
                    </Text>

                    <ScrollView>
                        {AllContacts.map((contact) => {
                            return (
                                <TouchableOpacity key={contact.contactUUID} style={[styles.SingleContact, {backgroundColor: contact.contactColor}]} onPress={() => {this.props.navigation.navigate('ContactDetailsView', {contactName: contact.contactName, contactPhoneNumber: contact.contactPhoneNumber, contactPhoto : contact.contactPhoto, contactUUID: contact.contactUUID, contactColor: contact.contactColor, loadContactUpdates: this.props.loadContactUpdates.bind(this), uniquePhoneNumbers: this.props.uniquePhoneNumbers})}}>

                                    <Image source={{uri: contact.contactPhoto}} style={styles.ContactImage}/>

                                    <View style={styles.ContactInfo}>
                                        <Text style={styles.ContactText}>
                                            {contact.contactName}
                                        </Text>
                                    </View>
                                </TouchableOpacity>
                            );
                        })}
                    </ScrollView>
                </View>
            )
        }
        // if All is empty we return a component with an empty contacts list message
        else {
            return (
                <View style={styles.ContactListEmpty}>
                    <Text style={GlobalStyles.HeaderText}>
                        You currently have no contacts
                    </Text>
                </View>
            )
        }
    }
}

export default withNavigation(ContactListComponent);

const styles = StyleSheet.create({
    ContactImage: {
        borderRadius: 30,
        height: 50,
        marginHorizontal: 30,
        marginVertical: 5,
        width: 50,
    },
    ContactInfo: {
        margin: '5%',
        marginHorizontal: 5,
    },
    ContactList: {
        height: 450,
        marginBottom: 15,
        maxHeight: '55%',
        width: '100%',
    },
    ContactListEmpty: {
        alignItems: 'center',
        height: 450,
        marginBottom: 15,
        maxHeight: '55%',
        width: '100%',
    },
    ContactListHeader: {
        fontSize: 20,
        fontWeight: 'bold',
        marginLeft: 20,
    },
    ContactText: {
        color: '#000000',
        fontSize: 18,
        marginBottom: 0,
    },
    NoContacts: {
        fontSize: 22,
        fontWeight: 'bold',
        marginVertical: 20,
        paddingBottom: 30,
    },
    SingleContact: {
        backgroundColor: '#eeeeee',
        borderRadius: 10,
        borderWidth: 1,
        color: '#ffffff',
        flexDirection: 'row',
        height: 60,
        marginHorizontal: 20,
        marginVertical : 5,
        width: '90%',
    },
});
