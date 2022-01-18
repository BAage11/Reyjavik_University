import * as FileSystem from 'expo-file-system';

// The directory of our app
export const DirectoryOfOurContacts = `${FileSystem.documentDirectory}TheContactor`;

// Create the directory whitin the phones file system if it doesn't already exist
export const createDirectory = async () => {
	const TheDirectory = await FileSystem.getInfoAsync(DirectoryOfOurContacts);
	if (!TheDirectory.exists) {
		await FileSystem.makeDirectoryAsync(DirectoryOfOurContacts);
	}
};

// Write the new contact within the apps directory
export const writeContactToFile = async (NewLocation, TheFile) => {
    FileSystem.writeAsStringAsync(NewLocation, TheFile)
};
