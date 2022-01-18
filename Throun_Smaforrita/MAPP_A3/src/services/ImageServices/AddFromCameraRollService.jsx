import * as ImageSelector from 'expo-image-picker';
import * as ThePermissions from 'expo-permissions';
import getPermission from './GetPermissionService';


// Function for asking permission to access the camera roll to select a contact image 
export const getImageFromCameraRoll = async () => {
    await getPermission([ ThePermissions.CAMERA_ROLL ]);
    const ImageSelection = await ImageSelector.launchImageLibraryAsync({
        mediaTypes: ImageSelector.MediaTypeOptions.Images,
        quality: .8,
    });

    if (ImageSelection.cancelled) {
        return 'https://www.techpowerusa.com/wp-content/uploads/2017/06/default-user.png';
    } else {
        return ImageSelection.uri;
    }
};
