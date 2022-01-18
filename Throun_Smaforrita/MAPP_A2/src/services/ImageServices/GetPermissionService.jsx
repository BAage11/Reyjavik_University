import * as Permissions from 'expo-permissions';

// Function for promting up a permission alert for accessing the camera roll / camera
const getPermission = async (ThePermissions) => {
    await Promise.all(ThePermissions.map(async type => await Permissions.askAsync(type)));
};

export default getPermission;
