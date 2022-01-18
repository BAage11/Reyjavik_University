import * as ImagePicker from 'expo-image-picker';
import * as Permissions from 'expo-permissions';

// ---------------------------------------------------------------------
// THESE FUNCTIONS ARE FROM THE PIXELMANIA PROJECT FROM THE LECTURES!
// ---------------------------------------------------------------------

// get permission from the user to allow their images to be used in the app
const getPermission = async permissionTypes => {
    await Promise.all(permissionTypes.map(async type => await Permissions.askAsync(type)));
};

// For fetching/selecting an image from the phones camera roll
export const selectFromCameraRoll = async () => {
    await getPermission([ Permissions.CAMERA_ROLL ]);
    const result = await ImagePicker.launchImageLibraryAsync({
        mediaTypes: ImagePicker.MediaTypeOptions.Images,
        quality: .8,
        base64: true,
        aspect: [16, 9]
    });
    if (result.cancelled) { return ''; }
    return result.uri;
};

// For opening up the camera in the phone, if the user allows it
export const takePhoto = async () => {
    await getPermission([ Permissions.CAMERA, Permissions.CAMERA_ROLL ]);
    const result = await ImagePicker.launchCameraAsync({
        mediaTypes: ImagePicker.MediaTypeOptions.Images,
        quality: .8,
        base64: true,
        aspect: [16, 9]
    });

    if (result.cancelled) { return ''; }
    return result.uri;
};
