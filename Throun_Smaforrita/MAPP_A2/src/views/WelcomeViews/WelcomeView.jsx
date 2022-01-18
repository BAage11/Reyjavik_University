import React from 'react';
import { Image, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { withNavigation } from 'react-navigation';
import { createDirectory } from '../../services/FileServices/WriteFileServices';
import GlobalStyles from '../../styles/GlobalStyles';
import logo from '../../../assets/logo.png';

// The page render when first opening up the app
class WelcomeView extends React.Component {
    constructor(props){
        super(props);
    }

    // Make sure our app directory exists, if not we create it
    async componentDidMount() {
        await createDirectory()
    }

    render () {
        // Make absolutely certain the apps directory exists
        createDirectory()
        return (
            <View style={[GlobalStyles.Container, {alignItems: 'center'}]}>
                <Image source={logo} style={styles.Logo}/>

                <TouchableOpacity style={GlobalStyles.Button} onPress={() => {this.props.navigation.navigate('ContactListView')}}>
                    <Text style={GlobalStyles.ButtonText}>
                        Let's get started!
                    </Text>
                </TouchableOpacity>
            </View>
        );
    }
}

export default withNavigation(WelcomeView);

const styles = StyleSheet.create({
    Logo: {
        height: 350,
        marginVertical: 80,
        maxHeight: '60%',
        width: 350,
    },
})
