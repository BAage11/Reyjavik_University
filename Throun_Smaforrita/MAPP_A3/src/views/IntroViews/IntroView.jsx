import React from 'react';
import { Image, StyleSheet, Text, View } from 'react-native';
import { withNavigation } from 'react-navigation';
import GlobalStyles from '../../styles/GlobalStyles';

// The page render when first opening up the app
class IntroView extends React.Component {
    constructor(props){
        super(props);
    }
    // When the component mounts
    componentDidMount() {
        // navigate to the cinema list view after 2,5 seconds
        setTimeout(()=>{ this.props.navigation.navigate("CinemasView") }, 2500);
    }
    //Render the component
    render () {
        // Fetch the logo
        const DrCinema = require('../../../assets/DrCinema.png')
        return (
            <View style={[GlobalStyles.Container, {alignItems: 'center'}]}>
                <Text style={styles.IntroText}>
                    Welcome!
                </Text>
                <Text style={GlobalStyles.NormalText}>
                    Let's watch some movies
                </Text>
                <Image source={DrCinema} style={styles.Logo}/>
            </View>
        );
    }
}

export default withNavigation(IntroView);

const styles = StyleSheet.create({
    Logo: {
        height: 350,
        marginHorizontal: '5%',
        marginVertical: '10%',
        maxHeight: '60%',
        width: '90%',
    },
    IntroText: {
        fontSize: 30,
        fontWeight: 'bold',
        marginTop: '20%',
        marginBottom: '3%'
    }
})
