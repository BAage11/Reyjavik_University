import { Alert } from 'react-native';
import * as Contacts from 'expo-contacts';
import * as FileSystem from 'expo-file-system';
import * as Permissions from 'expo-permissions';
import { cleanPhoneNumber, importContactsFailed, validateContactsFromOS, validateName } from './ValidationServices';
import { createDirectory, DirectoryOfOurContacts, writeContactToFile } from './WriteFileServices';

// Function for deleting a contact (file) from the apps directory
export const deleteExistingContact = async (FileName) => {
    FileSystem.deleteAsync(`${DirectoryOfOurContacts}/${FileName}`, { idempotent: true });
};

// Function for creating a new contact (file) within the apps DirectoryOfOurContacts
// If the contacts name is a valid string we create the user else show pop upalert.
export const createNewContact = async (ContactInfo) => {
    const ContactName = validateName(ContactInfo.contactName);
    if (ContactName) {
        const FileName = ContactName + '-' + ContactInfo.contactUUID + '.json';
        const JsonContact = JSON.stringify(ContactInfo);
        await writeContactToFile(`${DirectoryOfOurContacts}/${FileName}`, JsonContact);
    } else {
        Alert.alert(
            'Could not create contact:\n ' + ContactInfo.contactName,
            'This is probably due to the contacts name having unusual characters in it',
        );
    }
};

// Function for verifying the information from the OS contact list
// Same as the function above except it takes in a list of the current unique phone PhoneNumbers
// And doesn't import a user if the phone number already exists within the app
export const createNewContactFromOs = async (ContactInfo, uniquePhoneNumbers) => {
    const ContactName = validateName(ContactInfo.contactName);
    if (ContactName) {
        if (!uniquePhoneNumbers.includes(ContactInfo.contactPhoneNumber) || ContactInfo.contactPhoneNumber === '') {
    	    const FileName = ContactName + '-' + ContactInfo.contactUUID + '.json';
            const JsonContact = JSON.stringify(ContactInfo);
            await writeContactToFile(`${DirectoryOfOurContacts}/${FileName}`, JsonContact);
        }
    } else {
        Alert.alert(
            'Could not create contact:\n ' + ContactInfo.contactName,
            'This is probably due to the contacts name having unusual characters in it',
        );
    }
};

// Function for loading a single contact file into a json object
export const loadSingleContact = async (FileName) => {
    const SingleContact = FileSystem.readAsStringAsync(`${DirectoryOfOurContacts}/${FileName}`);
    return SingleContact;
};

// Deletes all contacts (files) from the apps directory
export async function deleteAllContacts () {
    const AllContactFiles = await FileSystem.readDirectoryAsync(DirectoryOfOurContacts);
    for(var i = 0; i < AllContactFiles.length; i++) {
        deleteExistingContact(AllContactFiles[i]);
    }
}

// Function for fetching all contacts within the app
export const loadAllContacts = async () => {
    const RetContacts = await FileSystem.readDirectoryAsync(DirectoryOfOurContacts);

    if (RetContacts.length > 0) {
        return (
            Promise.all(RetContacts.map(async (fileName) => {
    	       return JSON.parse( await loadSingleContact(fileName));
            }))
        );
    } else {
        return false;
    }
}

// A function which gets all the contact from the users phone OS and adds them to the app
export const loadAllContactsFromOS = async (loadContactUpdates, uniquePhoneNumbers) => {
    // First we check if the contact/directory exists, if not we create it
	await createDirectory();
	let NewContactArray = [];
    let FailedImports = [];

    // Get permission for retrieving contacts from the user device
	const { status } = await Contacts.requestPermissionsAsync();
	if (status === 'granted') {
		const contactsOS = await Contacts.getContactsAsync({
            fields: [
                Contacts.Fields.Name,
                Contacts.Fields.PhoneNumbers,
                Contacts.Fields.Image,
            ],
        });
        // If there are any contacts
        if (contactsOS) {
            // Validate the contact information for each contact imported
        	NewContactArray = (validateContactsFromOS(contactsOS.data, loadContactUpdates, cleanPhoneNumber));

            // For all the new contacts from the phones contacts list, create them within the apps directory
            NewContactArray.map(async (contact) => {
        		await createNewContactFromOs(contact, uniquePhoneNumbers);
        	});
            // Load updates for the contact list view, the function is passed here as a parameter from the ContaccListView
            loadContactUpdates();
        } else {
            // Alert if failed to get permission
            importContactsFailed();
        }
    }
};
