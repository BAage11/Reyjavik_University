import React from 'react';
import { Image, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { withNavigation } from 'react-navigation';


class NavigationComponent extends React.Component {
    constructor(props){
        super(props);
    }
    // render the view
    render () {
        return (
            <View style={styles.NavigationBar}>
                <TouchableOpacity style={styles.NavigationRoute} onPress={() => {this.props.navigation.navigate('CinemasView')}}>
                    <Text style={{fontWeight: 'bold', fontSize: 11}}>
                        Cinemas
                    </Text>
                </TouchableOpacity>

                <TouchableOpacity style={styles.NavigationRoute} onPress={() => {this.props.navigation.navigate('MovieListView')}}>
                    <Text style={{fontWeight: 'bold', fontSize: 11, textAlign: 'center'}}>
                        Currently{'\n'}Playing
                    </Text>
                </TouchableOpacity>

                <TouchableOpacity style={styles.NavigationRoute} onPress={() => {this.props.navigation.navigate('UpcomingReleasesView')}}>
                    <Text style={{fontWeight: 'bold', fontSize: 11, textAlign: 'center'}}>
                        Upcoming{'\n'}Releases
                    </Text>
                </TouchableOpacity>

                <TouchableOpacity style={styles.NavigationRoute} onPress={() => {this.props.navigation.navigate('UserProfileView', this.props)}}>
                    <Text style={{fontWeight: 'bold', fontSize: 10, textAlign: 'center', width: '70%'}}>
                        Your Favorites &{'\n'} Watch List
                    </Text>
                </TouchableOpacity>
            </View>
        );
    }
}

export default withNavigation(NavigationComponent);


const styles = StyleSheet.create({
    NavigationBar: {
        alignItems: 'flex-end',
        backgroundColor: '#ffffff',
        borderWidth: 0.2,
        bottom: 0,
        flexDirection: 'row',
        height: '8%',
        position: 'absolute',
        width: '100%',
    },
    NavigationLogo: {
        height: '50%',
        width: '50%',
    },
    NavigationRoute: {
        alignItems: 'center',
        borderWidth: 0.3,
        height: '100%',
        justifyContent: 'center',
        width: '25%',
    },
})
