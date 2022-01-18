import React from 'react';
import { Entypo } from '@expo/vector-icons';
import { StyleSheet, TouchableOpacity, View } from 'react-native';
import { withNavigation } from 'react-navigation';


// The component for adding images with either the camera or camera roll
class AddImageComponent extends React.Component {
    constructor(props){
        super(props);
    }

    // Render the component
    render() {
        return(
            <View style={styles.AddImageOptions}>
                <View style={styles.AddImageOptionsLayout}>
                    <TouchableOpacity onPress={() => this.props.cameraUpload()}>
                        <Entypo style={styles.CameraIcons} name="camera" />
                    </TouchableOpacity>

                    <TouchableOpacity onPress={() => this.props.cameraRollUpload()}>
                        <Entypo style={styles.CameraIcons} name="image" />
                    </TouchableOpacity>
                </View>
            </View>
        );
    }
}

export default withNavigation(AddImageComponent);

const styles = StyleSheet.create({
    AddImageOptions: {
        alignItems: 'center',
        marginBottom: 10,
        marginTop: 10,
    },
	AddImageOptionsLayout: {
		flexDirection: "row"
	},
	CameraIcons: {
		fontSize: 80,
		marginLeft: 20,
		marginRight: 20,
        marginTop: 0,
	},
});
