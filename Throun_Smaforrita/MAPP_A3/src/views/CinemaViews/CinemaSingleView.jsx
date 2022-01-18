import React from 'react';
import { Image, ScrollView, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { connect } from 'react-redux';
import GlobalStyles from '../../styles/GlobalStyles';
import HeaderComponent from '../../components/HeaderComponent';
import NavigationComponent from '../../components/NavigationComponent';
import LoadingComponent from '../../components/LoadingComponent';
import { getMovieListAction } from '../../actions/MovieListAction';


// The page render when first opening up the app
class CinemaSingleView extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            currentCinema: this.props.navigation.state.params,
            moviesInCinema: [],
            isLoading: true,
        }
    }
    // Function for when the component mounts
    async componentDidMount() {
        // fetch all movies
        await this.props.getMovieListAction();
        // find all movies playing in the given cinema
        const moviesInCinema = [];
        this.props.movieList.map((movie) => {
            for(var i = 0; i < movie.showtimes.length; i++) {
                if(movie.showtimes[i].cinema.id === this.state.currentCinema.id) {
                    moviesInCinema.push(movie);
                }
            }
        })
        // order the list alphabetically
        const orderedList = await this.alphabeticallyOrder(moviesInCinema)
        // Update the state
        await this.setState({moviesInCinema: orderedList});
        await this.setState({currentCinema: this.props.navigation.state.params});
        await this.setState({isLoading: false});
    }
    // A function for ordering a list into alphabetical order
    alphabeticallyOrder (MovieList) {
        MovieList.sort((MovieA, MovieB) => (MovieA.title < MovieB.title) ? -1 : 1);
        return MovieList
    }
    // Render the component
    render () {
        const {currentCinema, moviesInCinema, isLoading} = this.state;
        return (
            <View style={GlobalStyles.Container}>
                <HeaderComponent/>

                <View style={styles.CinemaInfo}>
                    <Text style={styles.PlayingHeader}>
                        {currentCinema.name}
                    </Text>

                    <Text style={GlobalStyles.NormalText}>
                        Phone: {currentCinema.phone}
                    </Text>

                    <Text style={GlobalStyles.NormalText}>
                        Website: {currentCinema.website}
                    </Text>

                    <Text style={GlobalStyles.NormalText}>
                        Address: {currentCinema['address\t']}, {currentCinema.city}
                    </Text>

                    <View style={styles.CinemaDescription}>
                        <ScrollView>
                            <View>
                                <Text style={{width: '90%', fontSize: 13}}>
                                    {'\n'}{currentCinema.description}
                                </Text>
                            </View>
                        </ScrollView>
                    </View>
                </View>

                <Text style={styles.PlayingHeader}>
                    Movies playing in {currentCinema.name}
                </Text>

                {isLoading ?
                    <View style={styles.MovieListWrapper}>
                        <LoadingComponent/>
                    </View>
                :

                    <View style={styles.MovieListWrapper}>
                        {moviesInCinema && moviesInCinema.length > 0 ?
                        <ScrollView>
                            {moviesInCinema.map((movie) => { return (
                                    <TouchableOpacity style={styles.SingleMovie} key={movie.id} onPress={() => this.props.navigation.navigate('MovieSingleView', [movie, currentCinema])}>
                                        <View style={{flexDirection: 'column'}}>
                                            <Text style={styles.SingleMovieHeader}>
                                                {movie.title} ({movie.year})
                                            </Text>

                                            <Text style={styles.SingleMovieText}>
                                                Genres:
                                            </Text>

                                            {movie.genres.map((genre) => {
                                                return (
                                                    <Text key={genre.ID} style={styles.SingleGenre}>
                                                        {genre['NameEN\t']}
                                                    </Text>
                                                );
                                            })}
                                        </View>

                                        <Image source={{uri: movie.poster}} style={styles.MoviePoster}/>
                                    </TouchableOpacity>
                            )})}
                        </ScrollView>
                        :
                        <View>
                            <Text>
                                No movies currently playing in this cinema
                            </Text>
                        </View>
                        }
                    </View>
                }
            <NavigationComponent/>
            </View>
        );
    }
}

const mapStateToProps = ({movieList}) => ({movieList});

export default connect(mapStateToProps, {getMovieListAction})(CinemaSingleView);

const styles = StyleSheet.create({
    CinemaDescription: {
        height: '60%',
        marginBottom: '3%',
        width: '90%',
    },
    CinemaInfo: {
        alignItems: 'flex-start',
        height: '35%',
        marginTop: '2%',
        width: '90%',
    },
    MovieListWrapper: {
        borderWidth: 0.2,
        height: '40%',
        width: '100%',
    },
    MoviePoster: {
        borderWidth: 0.5,
        height: '65%',
        marginBottom: '0%',
        marginRight: '5%',
        marginTop: '5%',
        position: 'absolute',
        right: 0,
        width: '20%',
    },
    PlayingHeader: {
        fontSize: 20,
        fontStyle: 'italic',
        fontWeight: 'bold',
        marginBottom: 5,
        marginTop: 5,
        textAlign: 'center',
    },
    SingleGenre: {
        fontSize: 10,
        marginLeft: '15%',
    },
    SingleMovie: {
        backgroundColor: '#ffffff',
        borderRadius: 5,
        borderWidth: 1,
        color: '#ffffff',
        flexDirection: 'row',
        height: 110,
        marginHorizontal: '1%',
        marginLeft: '5%',
        marginVertical : 5,
        width: '90%',
    },
    SingleMovieHeader: {
        fontSize: 14,
        fontWeight: 'bold',
        marginLeft: '5%',
    },
    SingleMovieText: {
        fontSize: 12,
        marginLeft: '5%',
    },
})
