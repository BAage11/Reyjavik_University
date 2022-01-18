import React from 'react';
import { ScrollView, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { WebView } from 'react-native-webview';
import Modal from 'react-native-modal';
import { connect } from 'react-redux';
import GlobalStyles from '../styles/GlobalStyles';


class TrailerComponent extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            trailers: this.props.trailers,
        }
    }
    // set the state to be sure when the component mounts
    async componentDidMount() {
        await this.setState({trailers: this.props.trailers});
    }
    // render the component
    render () {
        const {trailers} = this.state;
        return (
            <Modal isVisible={this.props.isTrailerModalOpen} animationIn='slideInDown' animationOut='slideOutUp' animationInTiming={1000} animationOutTiming={1000} transparent={false}>
                <View style={[GlobalStyles.Container, {backgroundColor: '#ffffff'}]}>
                    {trailers[0] && trailers[0].results.length > 0
                        ?
                        <View style={styles.TrailerList}>
                            <Text style={GlobalStyles.HeaderText}>
                                Trailers
                            </Text>

                            <ScrollView style={styles.TrailerWrapper}>
                            {trailers[0].results.map((trailer) => {
                                return (
                                <View style={styles.TrailerWrapper} key={trailer.id}>
                                    <Text style={styles.TrailerText}>
                                        {trailer.name}
                                    </Text>
                                    <WebView
                                        style={{marginTop: (Platform.OS == 'android') ? 20 : 0,}}
                                        source={{ uri: trailer.url }}
                                        domStorageEnabled={true}
                                        javaScriptEnabled={true}
                                        useWebKit={true}
                                   />
                                  </View>
                               );
                            })}
                            </ScrollView>
                        </View>
                        :
                        <View style={styles.NoTrailers}>
                            <Text style={GlobalStyles.HeaderText}>
                                Trailers
                            </Text>

                            <View style={styles.NoTrailersWrapper}>
                                <Text style={styles.TrailerText}>
                                    Unfortunately there are no trailers available for this movie
                                </Text>
                            </View>
                        </View>
                    }

                    <TouchableOpacity style={styles.CloseButton} onPress={() => {this.props.closeTrailerModal()}}>
                        <Text style={GlobalStyles.ButtonText}>
                            Close
                        </Text>
                    </TouchableOpacity>
                </View>
            </Modal>
        );
    }
}

export default connect(null, null)(TrailerComponent);

const styles = StyleSheet.create({
    CloseButton: {
        bottom: 10,
        position: 'absolute',
    },
    NoTrailers: {
        alignItems: 'center',
        height: '80%',
        marginTop: '15%',
        width: '100%',
    },
    NoTrailersWrapper: {
        alignItems: 'center',
        height: '100%',
        justifyContent: 'center',
        width: '100%',
    },
    Trailer: {
        backgroundColor: '#000000',
        height: '100%',
    },
    TrailerList: {
        alignItems: 'center',
        height: '80%',
        justifyContent: 'center',
        marginTop: '15%',
        width: '100%',
    },
    TrailerText: {
        fontSize: 20,
    },
    TrailerWrapper: {
        height: 220,
        marginHorizontal: '5%',
        marginVertical: '5%',
        width: '90%',
    },
})
