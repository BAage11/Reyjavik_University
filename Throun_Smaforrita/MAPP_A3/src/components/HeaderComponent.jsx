import React from 'react'
import { connect } from 'react-redux';
import { colors } from '../styles/GlobalStyles';
import { Image, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import UserEditProfileComponent from './UserEditProfileComponent';


class HeaderComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            isModalOpen: false,
        }
    }
    // open the edit profile view
    openModal() {
        this.setState({isModalOpen: true})
    }
    // close the edit profile view
    closeModal() {
        this.setState({isModalOpen: false})
    }

    // Render the component
    render() {
        return(
            <View style={styles.Header}>
                <UserEditProfileComponent isModalOpen={this.state.isModalOpen} closeModal={this.closeModal.bind(this)}/>

                <Text style={styles.UserName}>
                    {this.props.userInfo.userName}
                </Text>

                <View style={styles.UserProfile}>
                    <Image source={{uri: this.props.userInfo.userImage}} style={styles.UserImage}/>

                    <TouchableOpacity style={styles.EditProfileButton} onPress={() => this.openModal()}>
                        <Text style={styles.EditButtonText}>
                            Edit Profile
                        </Text>
                    </TouchableOpacity>
                </View>
            </View>
        )
    }
}

const mapStateToProps = ({userInfo}) => ({userInfo});

export default connect(mapStateToProps, null)(HeaderComponent);

const styles = StyleSheet.create({
    DrCinema: {
        fontSize: 14,
        left: '3%',
        position: 'absolute',
        top: '35%',
    },
    EditButtonText: {
        color: colors.darkBLue,
        fontSize: 12,
        top: 5
    },
    EditProfileButton: {
        top: '100%',
    },
    Header:{
        backgroundColor: '#ffffff',
        borderWidth: 0.2,
        flexDirection: 'row',
        height: '8%',
        width: '100%',
    },
    UserImage: {
        borderRadius: 20,
        height: '100%',
        left: 10,
        position: 'absolute',
        top: '10%',
        width: 35,
    },
    UserProfile: {
        flexDirection: 'column',
        left: 10,
        position: 'absolute',
        height: '60%'
    },
    UserName: {
        fontSize: 16,
        left: 60,
        position: 'absolute',
        top: '20%',
    },
})
