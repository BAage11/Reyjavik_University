import React from 'react';
import { StyleSheet, Text, TextInput, TouchableOpacity, View } from 'react-native';
import { withNavigation } from 'react-navigation';
import { deleteAllContactsConfirmation } from '../../services/FileServices/ValidationServices';
import { deleteAllContacts, loadAllContacts, loadAllContactsFromOS } from '../../services/FileServices/ContactFileServices';
import ContactListComponent from '../../components/ContactListComponent';
import GlobalStyles, { colors } from '../../styles/GlobalStyles';

// A function used for displaying only the contacts matching the search filter
async function filterUsingSearchValue (SearchValue, updateSearch, loadContactUpdates) {
    await updateSearch(SearchValue);
    await loadContactUpdates();
}

// The rendered page of the contact list
class ContactListView extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            uniquePhoneNumbers: [],
            currentContacts: [],
            currentSearch: '',
        }
    };

    // When the component mounts we load updates to the contact list
    async componentDidMount() {
        await this.loadContactUpdates();
    }

    // Update the state of the search value
    async updateSearch(SearchValue) {
        this.setState({currentSearch: SearchValue});
    }

    // The function used to load updates to the contact list
    async loadContactUpdates() {
        var AllContacts = await loadAllContacts();
        if (AllContacts) {
            AllContacts = await this.alphabeticallyOrder(AllContacts);
            AllContacts = await this.filterSearch(AllContacts)
        }
        this.setState({currentContacts: AllContacts});
        await this.updatePhonelist()
    }

    // Update the list of unique phone numbers to keep track of which phone numbers are taken
    async updatePhonelist() {
        if (this.state.currentContacts.length) {
            const newUniquePhoneNumbers = await this.state.currentContacts.map((contact) => {
                return contact.contactPhoneNumber
            });
            this.setState({uniquePhoneNumbers: newUniquePhoneNumbers});
        }
    }

    // Function which alphabetically orders the list based on the contacts name (contact.contactName)
    alphabeticallyOrder (AllContacts) {
        AllContacts.sort((contactA, contactB) => (contactA.contactName < contactB.contactName) ? -1 : 1);
        return AllContacts
    }

    // return a list of the contacts that match the search value
    filterSearch (AllContacts) {
        const FilteredContacts = AllContacts.filter((contact) => {
            return contact.contactName.toLowerCase().includes(this.state.currentSearch.toLowerCase());
        })
        return FilteredContacts;
    }

    // Render the view
    render() {
        // Fetch the curret contact list into a variable
        const AllContacts = this.state.currentContacts

        return (
            <View style={GlobalStyles.Container}>
                <View>
                    <TextInput autoCompleteType='off' autoCorrect={false} style={styles.Search} placeholder="Search for contact..." placeholderTextColor= '#000000' onChangeText={(value) => filterUsingSearchValue(value, this.updateSearch.bind(this), this.loadContactUpdates.bind(this))}/>
                </View>

                <ContactListComponent allContacts={AllContacts} loadContactUpdates={this.loadContactUpdates.bind(this)} uniquePhoneNumbers={this.state.uniquePhoneNumbers}>
                </ContactListComponent>

                <TouchableOpacity style={[GlobalStyles.Button]} onPress={() => {this.props.navigation.navigate('AddContactView', {loadContactUpdates: this.loadContactUpdates.bind(this), uniquePhoneNumbers: this.state.uniquePhoneNumbers})}}>
                    <Text style={GlobalStyles.ButtonText}>
                        Add a new contact
                    </Text>
                </TouchableOpacity>

                <TouchableOpacity style={[GlobalStyles.Button]} onPress={async () => await loadAllContactsFromOS(this.loadContactUpdates.bind(this), this.state.uniquePhoneNumbers)}>
                    <Text style={GlobalStyles.ButtonText}>
                        Import contacts from OS
                    </Text>
                </TouchableOpacity>

                <TouchableOpacity style={[GlobalStyles.Button]} onPress={async () => {await deleteAllContactsConfirmation(deleteAllContacts, this.loadContactUpdates.bind(this)); await this.setState({uniquePhoneNumbers: []})}}>
                    <Text style={GlobalStyles.ButtonText}>
                        Delete all contacts
                    </Text>
                </TouchableOpacity>
            </View>
        )
    }
}

export default withNavigation(ContactListView);

const styles = StyleSheet.create({
    ContactListHeader: {
        backgroundColor: colors.freshAir,
        color: '#000000',
        fontSize: 28,
        fontWeight: 'bold',
        height: 50,
        paddingTop: 5,
        textAlign: 'center',
        width: '100%',
    },
    Search:{
        backgroundColor: '#ffffff',
        borderRadius: 10,
        borderWidth: 1.2,
        color: '#000000',
        fontSize: 16,
        marginBottom: 10,
        padding: 8,
        width: 300,
        marginVertical: 20,
    },
})
