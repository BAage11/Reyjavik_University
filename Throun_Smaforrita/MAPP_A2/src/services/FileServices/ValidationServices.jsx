import 'react-native-get-random-values';
import { Alert } from 'react-native';
import { v4 as uuidV4 } from 'uuid';


// A map dictionary for turning non-latin characters into latin characters so that each file name can be read
const characterMap = {
    '-' : ' ',
    '-' : '_',
    'a' : 'á|à|ã|â|ä|á',
    'A' : 'À|Á|Ã|Â|Ä|Á',
    'e' : 'é|è|ê|ë|é',
    'E':  'É|È|Ê|Ë|É',
    'i' : 'í|ì|î|ï|í',
    'I' : 'Í|Ì|Î|Ï|Í',
    'o' : 'ó|ò|ô|õ|ö|ó',
    'O' : 'Ó|Ò|Ô|Õ|Ö|Ó',
    'u' : 'ú|ù|û|ü|ú',
    'U' : 'Ú|Ù|Û|Ü|Ú',
    'c' : 'ç|Ç',
    'n' : 'ñ|Ñ',
    'd' : 'ð',
    'D' : 'Ð',
    'ae': 'æ',
    'Ae': 'Æ',
    'th': 'þ',
    'Th': 'Þ',
};

// Function for creating a valid file name from the contacts name
export function validateName (TheName) {
    if (TheName) {
        // Replace spaces and special characters into a dash
        var NewName = TheName.replace(/\s/g, '-')
        // Replace all non-latin characters with latin characters using the map above
        for (var mapPattern in characterMap) {
            NewName = NewName.replace(new RegExp(characterMap[mapPattern], 'g'), mapPattern);
        }
        // Remove all other non-latin characters if any remain
        return NewName.replace(/[^A-Za-z0-9\s-]/g, '');
    }
    else{
        // Return false if the name was not a valid string
        return false;
    }
};
// Function for creating a valid phone number, used when importing contacts from the phones OS
export function cleanPhoneNumber (TheNumber) {
    // If the number is a valid string
    if (TheNumber) {
        // Remove spaces and special characters
    	var NewString = TheNumber.replace(/\s/g, '')
        // Remove all other non-latin characters if any remain
        NewString = NewString.replace(/[^A-Za-z0-9+\s-]/g, '');
        // Remove all dashes
        return NewString.replace(/-/g, '');
    }
};

// Function for getting conformation before deleting all contacts
export function deleteAllContactsConfirmation (deleteAllContacts, loadContactUpdates) {
    Alert.alert(
        'Are you sure?',
        'This will permenentely delete all your contacts from the app!',
        [
            {text: 'Yes', onPress: async () => {await deleteAllContacts(); await loadContactUpdates()}},
            {text: 'No', style: 'cancel'},
        ],
        {
            cancelable: true
        }
    );
}

// Function for getting conformation before deleting a single contacts
export function deleteSingleContactConfirmation (FileName, deleteExistingContact, loadUpdatesAndGoBack) {
    Alert.alert(
        'Are you sure?',
        'This will permenentely delete this contact from your app!',
        [
            {text: 'Yes', onPress: async () => {await deleteExistingContact(FileName); loadUpdatesAndGoBack()}},
            {text: 'No', style: 'cancel'},
        ],
        {
            cancelable: true
        }
    );
}

// Function for alerting if the import from the OS failed
export function importContactsFailed () {
    Alert.alert(
        'Error importing',
        'There were no contacts to import',
        [
            {text: 'OK'},
        ],
        {
            cancelable: true
        }
    );
}

// Function for alerting any missing / invalid input when creating / modifying a contact
export function inputIsMissingAddContact (message) {
    Alert.alert(
        'Input invalid!',
        message,
        [
            {text: 'OK'},
        ],
        {
            cancelable: true
        }
    );
}

// Create valid contact json objects from the imported contacts from the phones OS
export function validateContactsFromOS(contacts, loadContactUpdates, cleanPhoneNumber) {
	const ContactsToAdd = [];
	let CurrentContact = {};

    // Iterate through the imported contacts list
	for (var i = 1; i < contacts.length; i++) {
        CurrentContact = {};
        // Set the contact name
		CurrentContact.contactName = contacts[i].name;
        // Set the contacs phone if it exists, else blank
		if (contacts[i].phoneNumbers !== undefined) {
			CurrentContact.contactPhoneNumber = cleanPhoneNumber(contacts[i].phoneNumbers[0].number);
		} else {
			CurrentContact.contactPhoneNumber = '';
        }
        // set cotnacts photo if it exists, else default photo
		if (contacts[i].imageAvailable == true) {
			CurrentContact.contactPhoto = contacts[i].image.uri;
		} else {
			CurrentContact.contactPhoto = 'https://www.techpowerusa.com/wp-content/uploads/2017/06/default-user.png';
		}
        // Get a UUID for the user
        const UUID = uuidV4();
        // Set the contacts UUID and default color
        CurrentContact.contactUUID = UUID;
        CurrentContact.contactColor = '#eeeeee';
        // Push to the list of valid new contacts
		ContactsToAdd.push(CurrentContact);
	}
    // Return the valid contacts
	return ContactsToAdd;
}
