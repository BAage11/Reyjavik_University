import React from 'react';
import { ScrollView, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { WebView } from 'react-native-webview';
import Modal from 'react-native-modal';
import { connect } from 'react-redux';
import GlobalStyles from '../styles/GlobalStyles';


class RatingComponent extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            currentMovie: this.props.currentMovie,
        }
    }
    // update which movie we are rating
    async componentDidMount() {
        await this.setState({currentMovie: this.props.currentMovie});
    }

    render () {
        const movieForRating = this.props.movieForRating;
        return (
            <Modal isVisible={this.props.isRatingOpen} animationIn='slideInDown' animationOut='slideOutUp' animationInTiming={1000} animationOutTiming={500} transparent={false}>
                <View style={[GlobalStyles.Container, {backgroundColor: '#ffffff'}]}>
                    <Text style={[GlobalStyles.HeaderText, {marginTop: '15%'}]}>
                        Pick your rating for the movie:
                    </Text>

                    <View style={styles.RatingOptions}>
                        <TouchableOpacity style={styles.RatingButton} onPress={() => {this.props.addRatingToFavoriteMovie(movieForRating, 1); this.props.closeRatingModal()}}>
                            <Text style={GlobalStyles.HeaderText}>
                                1
                            </Text>
                        </TouchableOpacity>
                        <TouchableOpacity style={styles.RatingButton} onPress={() => {this.props.addRatingToFavoriteMovie(movieForRating, 2); this.props.closeRatingModal()}}>
                            <Text style={GlobalStyles.HeaderText}>
                                2
                            </Text>
                        </TouchableOpacity>
                        <TouchableOpacity style={styles.RatingButton} onPress={() => {this.props.addRatingToFavoriteMovie(movieForRating, 3); this.props.closeRatingModal()}}>
                            <Text style={GlobalStyles.HeaderText}>
                                3
                            </Text>
                        </TouchableOpacity>
                        <TouchableOpacity style={styles.RatingButton} onPress={() => {this.props.addRatingToFavoriteMovie(movieForRating, 4); this.props.closeRatingModal()}}>
                            <Text style={GlobalStyles.HeaderText}>
                                4
                            </Text>
                        </TouchableOpacity>
                        <TouchableOpacity style={styles.RatingButton} onPress={() => {this.props.addRatingToFavoriteMovie(movieForRating, 5); this.props.closeRatingModal()}}>
                            <Text style={GlobalStyles.HeaderText}>
                                5
                            </Text>
                        </TouchableOpacity>
                        <TouchableOpacity style={styles.RatingButton} onPress={() => {this.props.addRatingToFavoriteMovie(movieForRating, 6); this.props.closeRatingModal()}}>
                            <Text style={GlobalStyles.HeaderText}>
                                6
                            </Text>
                        </TouchableOpacity>
                        <TouchableOpacity style={styles.RatingButton} onPress={() => {this.props.addRatingToFavoriteMovie(movieForRating, 7); this.props.closeRatingModal()}}>
                            <Text style={GlobalStyles.HeaderText}>
                                7
                            </Text>
                        </TouchableOpacity>
                        <TouchableOpacity style={styles.RatingButton} onPress={() => {this.props.addRatingToFavoriteMovie(movieForRating, 8); this.props.closeRatingModal()}}>
                            <Text style={GlobalStyles.HeaderText}>
                                8
                            </Text>
                        </TouchableOpacity>
                        <TouchableOpacity style={styles.RatingButton} onPress={() => {this.props.addRatingToFavoriteMovie(movieForRating, 9); this.props.closeRatingModal()}}>
                            <Text style={GlobalStyles.HeaderText}>
                                9
                            </Text>
                        </TouchableOpacity>
                        <TouchableOpacity style={styles.RatingButton} onPress={() => {this.props.addRatingToFavoriteMovie(movieForRating, 10); this.props.closeRatingModal()}}>
                            <Text style={GlobalStyles.HeaderText}>
                                10
                            </Text>
                        </TouchableOpacity>
                    </View>


                    <TouchableOpacity style={styles.CloseButton} onPress={() => {this.props.closeRatingModal()}}>
                        <Text style={GlobalStyles.ButtonText}>
                            Close
                        </Text>
                    </TouchableOpacity>
                </View>
            </Modal>
        );
    }
}

export default connect(null, null)(RatingComponent);

const styles = StyleSheet.create({
    CloseButton: {
        bottom: 10,
        position: 'absolute',
    },
    RatingOptions: {
        height: '80%',
        width: '80%',
        alignItems: 'center',
        justifyContent: 'center',
    },
    RatingButton: {
        height: '6%',
        width: '60%',
        backgroundColor: '#ffffff',
        borderWidth: 1,
        alignItems: 'center',
        justifyContent: 'center',
        marginVertical: '3%',
        borderRadius: 30,
    }
})
