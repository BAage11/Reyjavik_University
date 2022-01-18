import React from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image, TouchableOpacity, Button, SafeAreaView } from 'react-native';
import GlobalStyles from '../../styles/GlobalStyles';

// the page rendered when the user first opens up the app
const MainView = ({ navigation: { navigate } }) => {
    return (
        <View style={GlobalStyles.container}>
            <Text style={styles.Header}>
                Toddler
            </Text>

            <Image
                style={styles.ToddlerImage}
                source={require('../../../assets/todo_list2.png')}
            />

            <Text style={styles.WelcomeText}>
                Welcome to the Toodler app!
            </Text>

            <TouchableOpacity style={styles.GetStartedButton} onPress={() => navigate('BoardListView')}>
                <Text style={styles.GetStartedButtonText}>
                    Let's get started!
                </Text>
            </TouchableOpacity>
        <StatusBar style='auto' />
        </View>
    );
}

export default MainView

const styles = StyleSheet.create({
    GetStartedButton: {
        alignItems: 'center',
        backgroundColor: '#000000',                       // '#eeeeee',
        borderColor: '#ffffff',
        borderWidth: 3,
        height: 60,
        width: 200,
    },
    GetStartedButtonText: {
        color: '#ffffff',
        fontSize: 18,
        fontWeight: 'bold',
        height: 60,
        marginVertical: 12,
        textAlign: 'center',
    },
    Header: {
        fontSize: 70,
        fontWeight: 'bold',
        height: 120,
        top: 20,
    },
    ToddlerImage: {
        height: '50%',
        resizeMode: 'stretch',
        width: '80%',
      },
    WelcomeText: {
        color: '#ffffff',
        fontSize: 20,
        height: 40,
        marginVertical: 20,
        textAlign: 'center',
    },
});
