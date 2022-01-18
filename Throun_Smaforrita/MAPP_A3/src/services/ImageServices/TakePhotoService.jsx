import * as ImageSelector from 'expo-image-picker';
import * as ThePermissions from 'expo-permissions';
import getPermission from './GetPermissionService';


// Function for accessing the camera to take a phot for a contact image
export const getImageByCamera = async () => {
    await getPermission([ ThePermissions.CAMERA, ThePermissions.CAMERA_ROLL ]);
    const result = await ImageSelector.launchCameraAsync({
        mediaTypes: ImageSelector.MediaTypeOptions.Images,
        quality: .8,
        base64: true,
        aspect: [16, 9]
    });

    if (result.cancelled) {
        return 'https://www.techpowerusa.com/wp-content/uploads/2017/06/default-user.png';
    } else {
        return result.uri;
    }
};
