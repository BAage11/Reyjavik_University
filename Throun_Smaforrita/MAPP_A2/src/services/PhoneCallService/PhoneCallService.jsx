import { Linking, Alert, Platform } from 'react-native';

// Function for making a mobile phone call to contact number within the app
export const MakePhoneCall = contactPhone => {
    let phoneNumber = contactPhone;
    // Distinguish between Android and IOS phones - different methods
    if (Platform.OS !== 'android') {
        phoneNumber = `telprompt:${contactPhone}`;
    } else  {
        phoneNumber = `tel:${contactPhone}`;
    }
    // Try to make the phonecall for given phone number
    Linking.canOpenURL(phoneNumber).then(supported => {
        if (!supported) {
            Alert.alert('Contact/Phone number not available');
        } else {
            return Linking.openURL(phoneNumber);
        }
    })
};
