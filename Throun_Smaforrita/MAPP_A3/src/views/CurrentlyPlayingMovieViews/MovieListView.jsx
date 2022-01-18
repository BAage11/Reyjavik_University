import React from 'react';
import { Image, ScrollView, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { connect } from 'react-redux';
import GlobalStyles from '../../styles/GlobalStyles';
import HeaderComponent from '../../components/HeaderComponent';
import NavigationComponent from '../../components/NavigationComponent';
import LoadingComponent from '../../components/LoadingComponent';
import { getMovieListAction } from '../../actions/MovieListAction';


// The page render when first opening up the app
class MovieListView extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            movieList: this.props.movieList,
            isLoading: true,
            currentGenreFilter: 'None'
        }
    }
    // when the component mounts
    async componentDidMount() {
        // Fetch a list of all movies playing
        await this.props.getMovieListAction();
        // update the state
        await this.setState({movieList: this.alphabeticallyOrder(this.props.movieList)})
        await this.setState({isLoading: false});
    }
    // A function for alphabetically ordering all the movies in the list
    alphabeticallyOrder (AllMovies) {
        AllMovies.sort((movieA, movieB) => (movieA.title < movieB.title) ? -1 : 1);
        return AllMovies
    }
    // Filtering out only the movies in the selected genre
    async filterGenre (genreFilter) {
        if(genreFilter !== 'None') {
            await this.setState({isLoading: true});
            //await this.props.upcomingMoviesAction();
            const AllMovies = this.props.movieList;
            const FilteredMovies = []
            await AllMovies.filter((movie) => {
                movie.genres.filter((genre) => {
                    if(genre['NameEN\t'] === genreFilter) {
                        FilteredMovies.push(movie);
                    }
                })
            })
            // Update the state
            await this.setState({movieList: this.alphabeticallyOrder(FilteredMovies)});
            await this.setState({isLoading: false});
        }
        else{
            // If no filter is selected then we display all movies in alphabetical order
            await this.setState({movieList: this.alphabeticallyOrder(this.props.movieList)});
        }
    }
    // Render the component
    render () {
        const {movieList, isLoading, currentGenreFilter} = this.state
        return (
            <View style={GlobalStyles.Container}>
                <HeaderComponent/>

                {isLoading ?
                    <View style={styles.MovieListWrapper}>
                        <Text style={[GlobalStyles.HeaderText, {marginBottom: 10, marginLeft: '5%',}]}>
                            Movies Currently In Cinemas:
                        </Text>

                        <LoadingComponent/>
                    </View>
                :
                    <View style={styles.MovieListWrapper}>
                        <Text style={[GlobalStyles.HeaderText, {marginBottom: 10, marginLeft: '5%',}]}>
                            Movies Currently In Cinemas:
                        </Text>

                        <Text style={styles.GenreText}>
                            Genre filter:
                        </Text>

                        <View style={styles.GenreFilterWrapper}>
                            <TouchableOpacity style={currentGenreFilter === 'None' ? styles.GenreFilterButtonSelected : styles.GenreFilterButtonNotSelected} onPress={() => {this.filterGenre('None'); this.setState({currentGenreFilter: 'None'})}}>
                                <Text style={styles.GenreButtonText}>
                                    No filter
                                </Text>
                            </TouchableOpacity>
                            <TouchableOpacity style={currentGenreFilter === 'Action' ? styles.GenreFilterButtonSelected : styles.GenreFilterButtonNotSelected} onPress={() => {this.filterGenre('Action'); this.setState({currentGenreFilter: 'Action'})}}>
                                <Text style={styles.GenreButtonText}>
                                    Action
                                </Text>
                            </TouchableOpacity>
                            <TouchableOpacity style={currentGenreFilter === 'Adventure' ? styles.GenreFilterButtonSelected : styles.GenreFilterButtonNotSelected} onPress={() => {this.filterGenre('Adventure'); this.setState({currentGenreFilter: 'Adventure'})}}>
                                <Text style={styles.GenreButtonText}>
                                    Adventure
                                </Text>
                            </TouchableOpacity>
                            <TouchableOpacity style={currentGenreFilter === 'Comedy' ? styles.GenreFilterButtonSelected : styles.GenreFilterButtonNotSelected} onPress={() => {this.filterGenre('Comedy'); this.setState({currentGenreFilter: 'Comedy'})}}>
                                <Text style={styles.GenreButtonText}>
                                    Comedy
                                </Text>
                            </TouchableOpacity>
                            <TouchableOpacity style={currentGenreFilter === 'Crime' ? styles.GenreFilterButtonSelected : styles.GenreFilterButtonNotSelected} onPress={() => {this.filterGenre('Crime'); this.setState({currentGenreFilter: 'Crime'})}}>
                                <Text style={styles.GenreButtonText}>
                                    Crime
                                </Text>
                            </TouchableOpacity>
                        </View>
                        <View style={styles.GenreFilterWrapper}>
                            <TouchableOpacity style={currentGenreFilter === 'Drama' ? styles.GenreFilterButtonSelected : styles.GenreFilterButtonNotSelected} onPress={() => {this.filterGenre('Drama'); this.setState({currentGenreFilter: 'Drama'})}}>
                                <Text style={styles.GenreButtonText}>
                                    Drama
                                </Text>
                            </TouchableOpacity>
                            <TouchableOpacity style={currentGenreFilter === 'Horror' ? styles.GenreFilterButtonSelected : styles.GenreFilterButtonNotSelected} onPress={() => {this.filterGenre('Horror'); this.setState({currentGenreFilter: 'Horror'})}}>
                                <Text style={styles.GenreButtonText}>
                                    Horror
                                </Text>
                            </TouchableOpacity>
                            <TouchableOpacity style={currentGenreFilter === 'Romance' ? styles.GenreFilterButtonSelected : styles.GenreFilterButtonNotSelected} onPress={() => {this.filterGenre('Romance'); this.setState({currentGenreFilter: 'Romance'})}}>
                                <Text style={styles.GenreButtonText}>
                                    Romance
                                </Text>
                            </TouchableOpacity>
                            <TouchableOpacity style={currentGenreFilter === 'Sci-Fi' ? styles.GenreFilterButtonSelected : styles.GenreFilterButtonNotSelected} onPress={() => {this.filterGenre('Sci-Fi'); this.setState({currentGenreFilter: 'Sci-Fi'})}}>
                                <Text style={styles.GenreButtonText}>
                                    Sci-Fi
                                </Text>
                            </TouchableOpacity>
                            <TouchableOpacity style={currentGenreFilter === 'Thriller' ? styles.GenreFilterButtonSelected : styles.GenreFilterButtonNotSelected} onPress={() => {this.filterGenre('Thriller'); this.setState({currentGenreFilter: 'Thriller'})}}>
                                <Text style={styles.GenreButtonText}>
                                    Thriller
                                </Text>
                            </TouchableOpacity>
                        </View>

                        <ScrollView>
                            {movieList.map((movie) => {
                                return(
                                    <TouchableOpacity key={movie.id+'-'+movie.name} style={styles.SingleMovie} onPress={() => this.props.navigation.navigate('CurrentlyPlayingMovieSingleView', movie)}>
                                        <View style={styles.SingleMovieInfo}>
                                            <Text style={styles.SingleMovieHeader}>
                                              {movie.title}
                                            </Text>
                                            <Text style={styles.SingleMovieText}>
                                                {movie.year}
                                            </Text>

                                            <Text style={styles.SingleMovieText}>
                                                Genres:
                                            </Text>

                                            <View style={styles.Genres}>
                                            {movie.genres.map((genre, index) => {
                                                return (
                                                    <Text key={movie.id + '-' + genre['NameEN\t'] + '-' + index} style={styles.SingleGenre}>
                                                        {genre['NameEN\t']}
                                                    </Text>
                                                );
                                            })}
                                            </View>
                                        </View>

                                        <Image source={{uri: movie.poster}} style={styles.MoviePoster}/>
                                    </TouchableOpacity>
                                );
                            })}
                        </ScrollView>
                    </View>
                }
            <NavigationComponent/>
            </View>
        );
    }
}

const mapStateToProps = ({movieList}) => ({movieList});

export default connect(mapStateToProps, {getMovieListAction})(MovieListView);

const styles = StyleSheet.create({
    GenreButtonText: {
        fontSize: 8,
    },
    GenreFilterButtonSelected:{
        alignItems: 'center',
        justifyContent: 'center',
        height: 20,
        width: 60,
        backgroundColor: '#ffffff',
        borderWidth: 2,
        borderRadius: 15,
        marginBottom: '2%',
        marginHorizontal: '1.5%',
        fontWeight: 'bold'

    },
    GenreFilterButtonNotSelected:{
        alignItems: 'center',
        justifyContent: 'center',
        height: 20,
        width: 60,
        backgroundColor: '#EDF8DF',
        borderWidth: 1,
        borderRadius: 15,
        marginBottom: '2%',
        marginHorizontal: '1.5%',

    },
    GenreFilterWrapper:{
        flexDirection: 'row',
        alignItems: 'center',
        justifyContent: 'center'
    },
    Genres: {
        flexDirection: 'row',
        marginLeft: '5%',
    },
    GenreText: {
        marginLeft: '4%',
        marginBottom: '1%',
    },
    MovieListWrapper: {
        height: '80%',
        marginTop: '2%',
        width: '100%',
    },
    MoviePoster: {
        height: '85%',
        marginVertical: '1%',
        marginRight: '5%',
        position: 'absolute',
        right: 0,
        width: '10%',
    },
    SingleGenre: {
        fontSize: 10,
        fontStyle: 'italic',
        marginLeft: '2%',
    },
    SingleMovieHeader: {
        fontSize: 12,
        fontWeight: 'bold',
    },
    SingleMovie: {
        backgroundColor: '#ffffff',
        borderRadius: 10,
        borderWidth: 1,
        flexDirection: 'row',
        height: 80,
        marginHorizontal: '5%',
        marginVertical : 5,
        width: '90%',
    },
    SingleMovieInfo: {
        justifyContent: 'center',
        marginLeft: 10,
    },
    SingleMovieText: {
        fontSize: 12,
    },
})
