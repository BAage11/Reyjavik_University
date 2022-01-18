import React from 'react';
import { Image, StyleSheet, Text, TextInput, TouchableOpacity, View } from 'react-native';
import Modal from 'react-native-modal';
import { connect } from 'react-redux';
import GlobalStyles from '../styles/GlobalStyles';
import AddImageComponent from '../components/AddImageComponent';
import { changeUserInfo } from '../actions/UserActions';
import { getImageFromCameraRoll } from '../services/ImageServices/AddFromCameraRollService';
import { getImageByCamera } from '../services/ImageServices/TakePhotoService';


// The page render when first opening up the app
class UserEditProfileComponent extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            userName: this.props.userInfo.userName,
            userImage: this.props.userInfo.userImage,
        }
    }
    // update the state ones the suername is changed
    nameInputHandler(updatedName) {
        this.setState({userName: updatedName});
    }
    // load image from camera roll
     async cameraRollUpload() {
        const NewPhoto = await getImageFromCameraRoll();
        this.setState({userImage: NewPhoto})
    }

    // Add photo to contact via taking a photo
    async cameraUpload () {
        const NewPhoto = await getImageByCamera();
        this.setState({userImage: NewPhoto});
    }
    // handle changes being saved
    onPressHandler() {
        const {userName, userImage} = this.state;
        this.props.changeUserInfo(userName, userImage);
    }
    // render the component
    render () {
        return (
            <Modal isVisible={this.props.isModalOpen} animationIn='slideInDown' animationOut='slideOutUp' animationInTiming={500} animationOutTiming={500} transparent={false}>

                <View style={[GlobalStyles.Container, {backgroundColor: '#ffffff', justifyContent: 'center'}]}>
                    <Text style={GlobalStyles.HeaderText}>
                        {this.state.userName}
                    </Text>

                    <Image source={{uri: this.state.userImage}} style={styles.UserProfileImage}/>

                    <AddImageComponent cameraUpload={this.cameraUpload.bind(this)} cameraRollUpload={this.cameraRollUpload.bind(this)}/>


                    <TextInput style={GlobalStyles.TextInput} placeholder='Enter name' onChangeText={text => this.setState({userName: text})} autoCompleteType='off' autoCorrect={false} placeholderTextColor='grey' returnKeyType='done'/>

                    <TouchableOpacity style={GlobalStyles.Button} onPress={() => {this.onPressHandler(); this.props.closeModal()}}>
                        <Text style={GlobalStyles.ButtonText}>
                            Save changes
                        </Text>
                    </TouchableOpacity>

                    <TouchableOpacity style={GlobalStyles.Button} onPress={() => {this.props.closeModal()}}>
                        <Text style={GlobalStyles.ButtonText}>
                            Cancel
                        </Text>
                    </TouchableOpacity>
                </View>
            </Modal>

        );
    }
}

const mapStateToProps = ({userInfo}) => ({userInfo});

export default connect(mapStateToProps, { changeUserInfo })(UserEditProfileComponent);

const styles = StyleSheet.create({
    UserProfileImage: {
        backgroundColor: '#000000',
        borderRadius: 120,
        borderWidth: 2,
        height: '25%',
        marginTop: '5%',
        width: '60%',
    },
})
