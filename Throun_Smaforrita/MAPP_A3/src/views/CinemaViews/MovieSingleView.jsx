import React from 'react';
import { Alert, Image, Linking, ScrollView, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { connect } from 'react-redux';
import GlobalStyles from '../../styles/GlobalStyles';
import HeaderComponent from '../../components/HeaderComponent';
import NavigationComponent from '../../components/NavigationComponent';
import TrailerComponent from '../../components/TrailerComponent';
import { addToMovieList } from '../../services/AddOrRemoveFromListServices/AddMovieToList';
import { watchListAction } from '../../actions/WatchListAction';


// The page render when first opening up the app
class MovieSingleView extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            currentMovie: this.props.navigation.state.params[0],
            currentCinema: this.props.navigation.state.params[1],
            isTrailerModalOpen: false,
        }
    }

    async componentDidMount() {
    }
    // open the trailer modal
    openTrailerModal() {
        this.setState({isTrailerModalOpen: true});
    }
    // close the trailer modal
    closeTrailerModal() {
        this.setState({isTrailerModalOpen: false});
    }
    // a funciton for adding a movie to the users watch list
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
    // Render the component
    render () {
        const {currentMovie, currentCinema, isTrailerModalOpen} = this.state;

        return (
            <View style={GlobalStyles.Container}>
                <TrailerComponent isTrailerModalOpen={isTrailerModalOpen} trailers={currentMovie.trailers} closeTrailerModal={this.closeTrailerModal.bind(this)}/>

                <HeaderComponent/>

                <View style={styles.MovieInfoWrapper}>
                    <View style={styles.MovieInfo}>
                        <Text style={styles.MovieInfoHeader}>
                            {currentCinema.name}
                        </Text>

                        <Text style={styles.MovieInfoHeader}>
                            {currentMovie.title} ({currentMovie.year}) - { Number(currentMovie.durationMinutes) > 0 ?  currentMovie.durationMinutes + ' minutes' : 'Duration unknown'}
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
                    </View>

                    <View style={styles.GenresWrapper}>
                        <Text style={styles.MovieInfoHeader}>
                            Genres:
                        </Text>

                        <View style={styles.Genres}>
                            {currentMovie.genres.map((genre, index) => {
                                return (
                                    <Text key={genre.ID + '-' + genre.Name + '-' + index} style={styles.SingleGenre}>
                                        {genre['NameEN\t']}
                                    </Text>
                                );
                            })}
                        </View>
                    </View>

                    <View style={styles.ShowtimesWrapper}>
                        <Text style={styles.MovieInfoHeader}>
                            Showtimes in {currentCinema.name}:
                        </Text>

                        <ScrollView style={styles.Showtimes}>
                            {currentMovie.showtimes.map((showtime) => {
                                if (showtime.cinema.id === currentCinema.id) {
                                    return (
                                        showtime.schedule.map((schedule, index) => {
                                            return (
                                                <View style={styles.MovieTimeRow} key={showtime.cinema.name+'-'+schedule.time + '-' + index} >
                                                    <Text style={styles.MovieTime}>
                                                        {schedule.time}
                                                    </Text>

                                                    <TouchableOpacity style={styles.TicketButton} onPress={() => Linking.openURL(schedule.purchase_url)}>
                                                        <Text>
                                                            Buy ticket(s)
                                                        </Text>
                                                    </TouchableOpacity>
                                                </View>
                                            )
                                        })
                                    );
                                }
                            })}
                        </ScrollView>
                    </View>
                </View>
            <NavigationComponent/>
            </View>
        );
    }
}

const mapStateToProps = ({watchList}) => ({watchList});

export default connect(mapStateToProps, {watchListAction})(MovieSingleView);

const styles = StyleSheet.create({
    CinemaName: {
        fontSize: 20,
        fontWeight: 'bold',
    },
    Genres: {
        flexDirection: 'row',
    },
    GenresWrapper: {
        height: '10%',
        marginTop: '10%',
        width: '100%'
    },
    MovieInfo: {
        alignItems: 'flex-start',
        height: '40%',
        marginBottom: '15%',
        width: '90%',
    },
    MovieInfoHeader: {
        fontSize: 18,
        fontWeight: 'bold',
        marginBottom: '1%',
        marginTop: '2%',
    },
    MovieInfoWrapper: {
        height: '85%',
        width: '95%',
    },
    MovieName: {
        fontSize: 20,
        fontWeight: 'bold',
    },
    MoviePlot: {
        fontSize: 12,
        marginLeft: '5%',
    },
    MoviePoster: {
        borderWidth: 1.5,
        height: '45%',
        marginHorizontal: '30%',
        marginTop: '2%',
        width: '50%',
    },
    MovieTime: {
        fontSize: 20,
        fontWeight: 'bold',
        marginTop: '2%',
    },
    MovieTimeRow: {
        flexDirection: 'row',
        marginLeft: '10%',
        marginVertical: '4%',
    },
    PlotDescription: {
        height: '25%',
        marginBottom: '5%',
        width: '100%',
    },
    SingleGenre:??{
        fontSize: 12,
        marginHorizontal: '2%',
        marginLeft: '5%',
    },
    Showtimes:{
        backgroundColor: '#ffffff',
        borderRadius: 20,
        borderWidth: 1,
    },
    ShowtimesWrapper:{
        height: '30%',
        width: '100%',
    },
    TicketButton: {
        alignItems: 'center',
        backgroundColor: '#ffffff',
        borderRadius: 20,
        borderWidth: 1.5,
        height: 40,
        justifyContent: 'center',
        position: 'absolute',
        right: '10%',
        width: 150,
    },
    TrailerButton:??{
        alignItems: 'center',
        backgroundColor: '#ffffff',
        borderRadius: 20,
        borderWidth: 2,
        height: 40,
        justifyContent: 'center',
        marginHorizontal: 5,
        width: '50%',
        marginHorizontal: '2%'

    },
    TrailerButtonWrapper:??{
        alignItems: 'center',
        flexDirection: 'row',
        justifyContent: 'center',
        marginHorizontal: '5%',
        marginTop: 10,
        width: '100%',
    },
})
