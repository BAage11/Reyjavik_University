import React from 'react';
import { Alert, Image, ScrollView, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { connect } from 'react-redux';
import GlobalStyles from '../../styles/GlobalStyles';
import HeaderComponent from '../../components/HeaderComponent';
import NavigationComponent from '../../components/NavigationComponent';
import TrailerComponent from '../../components/TrailerComponent';
import { addToMovieList } from '../../services/AddOrRemoveFromListServices/AddMovieToList';
import { watchListAction } from '../../actions/WatchListAction';


// The page render when first opening up the app
class UpcomingMovieSingleView extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            currentMovie: this.props.navigation.state.params,
            isTrailerModalOpen: false,
        }
    }
    // When the component mounts
    async componentDidMount() {
        await this.setState({currentMovie: this.props.navigation.state.params});
    }
    // Open the trailer modal
    openTrailerModal() {
        this.setState({isTrailerModalOpen: true});
    }
    // Close the trailer modal
    closeTrailerModal() {
        this.setState({isTrailerModalOpen: false});
    }

    async addMovieToWatchList() {
        // get the watch list
        const watchList = this.props.watchList;
        // find the length of the watch list
        const oldLengthOfList = watchList.length;
        // add movie to the watch list
        const newWatchList = await addToMovieList(watchList, this.state.currentMovie);
        // Find the lenght of the new watch list
        const newLengthOfList = newWatchList.length;
        // If the list gets longer the movie was added
        if (oldLengthOfList < newLengthOfList){
            await this.props.watchListAction(newWatchList);
            Alert.alert(
                'Movie was added to your Watch List',
            )
        }
        // the movie was already within the list
        else{
            Alert.alert(
                'Movie already in your Watch List',
            )
        }
    }
    //Render the component
    render () {
        const {currentMovie, isTrailerModalOpen} = this.state;
        return (
            <View style={GlobalStyles.Container}>
                <TrailerComponent isTrailerModalOpen={isTrailerModalOpen} trailers={currentMovie.trailers} closeTrailerModal={this.closeTrailerModal.bind(this)}/>

                <HeaderComponent/>

                <View style={styles.MovieInfo}>
                    <Text style={styles.MovieName}>
                        {currentMovie.title} ({currentMovie['release-dateIS']})
                    </Text>

                    <Image source={{uri: currentMovie.poster}} style={styles.MoviePoster}/>

                    <View style={styles.TrailerButtonWrapper}>
                        <TouchableOpacity style={styles.TrailerButton} onPress={() => this.openTrailerModal()}>
                            <Text>
                                View Trailers
                            </Text>
                        </TouchableOpacity>

                        <TouchableOpacity style={styles.TrailerButton} onPress={() => this.addMovieToWatchList()}>
                            <Text>
                                Add to Watch List
                            </Text>
                        </TouchableOpacity>
                    </View>

                    <Text style={styles.MovieInfoHeader}>
                        Plot:
                    </Text>

                    <View style={styles.PlotDescription}>
                        <ScrollView>
                            <View>
                                <Text style={styles.MoviePlot}>
                                    {currentMovie.omdb[0].Plot}
                                </Text>
                            </View>
                        </ScrollView>
                    </View>

                    <Text style={styles.MovieInfoHeader}>
                        Genres:
                    </Text>

                    <View style={styles.Genres}>
                        {this.state.currentMovie.genres.map((genre, index) => {
                            return (
                                <Text key={genre.ID + '-' + index} style={styles.SingleGenre}>
                                    {genre['NameEN\t']}
                                </Text>
                            );
                        })}
                    </View>
                </View>
            <NavigationComponent/>
            </View>
        );
    }
}

const mapStateToProps = ({watchList, favoritesList}) => ({watchList, favoritesList});

export default connect(mapStateToProps, {watchListAction})(UpcomingMovieSingleView);

const styles = StyleSheet.create({
    Genres: {
        flexDirection: 'row',
        width: '100%'
    },
    MovieInfo: {
        height: '100%',
        marginTop: 10,
        width: '95%',
    },
    MovieInfoHeader: {
        fontSize: 16,
        fontWeight: 'bold',
        marginTop: '5%',
    },
    MovieName: {
        fontSize: 20,
        fontWeight: 'bold',
        marginBottom: 10,
    },
    MoviePoster: {
        height: '35%',
        marginHorizontal: '25%',
        marginTop: '1%',
        width: '45%',
    },
    MovieTime: {
        fontSize: 20,
        fontWeight: 'bold',
        marginTop: '2%',
    },
    MovieTimeRow: {
        flexDirection: 'row',
        marginLeft: '10%',
        marginVertical: '2%',
    },
    PlotDescription: {
        height: '12%',
        width: '100%',
    },
    SingleGenre: {
        marginHorizontal: '2%',
    },
    TrailerButton: {
        alignItems: 'center',
        backgroundColor: '#ffffff',
        borderRadius: 20,
        borderWidth: 2,
        height: 40,
        justifyContent: 'center',
        width: 150,
        marginHorizontal: '2%'
    },
    TrailerButtonWrapper: {
        alignItems: 'center',
        flexDirection: 'row',
        justifyContent: 'center',
        marginTop: 10,
        width: '100%',
    },
})
