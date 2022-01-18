import React from 'react';
import { Image, StyleSheet, View } from 'react-native';


class LoadingComponent extends React.Component {
    constructor(props){
        super(props);
    }
    // the gif that shows when the lists are loading
    render () {
        const loadingGif = require('../../assets/ajax_loader.gif');

        return (
            <View style={styles.LoadingComponent}>
                <Image source={loadingGif} style={styles.LoadingGif}/>
            </View>
        );
    }
}

export default LoadingComponent;

const styles = StyleSheet.create({
    LoadingComponent: {
        alignItems: 'center',
        backgroundColor: '#EDF8DF',
        height: '100%',
        justifyContent: 'center',
        width: '100%',
    },
    LoadingGif: {
        height: '40%',
        width: '40%',
    },
})
