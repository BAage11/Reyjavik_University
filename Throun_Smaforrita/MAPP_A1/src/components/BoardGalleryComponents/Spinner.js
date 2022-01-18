import React from 'react';
import { View, ActivityIndicator, StyleSheet } from 'react-native';


// the loading symbol showd if the images are being loaded
const Spinner = () => (
    <View style={ styles.Spinner }>
        <ActivityIndicator color="black" />
    </View>
);

export default Spinner;

const styles = StyleSheet.create({
    Spinner: {
        alignItems: 'center',
        flex: 1,
        justifyContent: 'center',
    },
});
