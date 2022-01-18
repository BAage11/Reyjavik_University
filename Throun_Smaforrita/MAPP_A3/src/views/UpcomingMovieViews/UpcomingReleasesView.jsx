import React from 'react';
import { Image, ScrollView, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { connect } from 'react-redux';
import GlobalStyles from '../../styles/GlobalStyles';
import HeaderComponent from '../../components/HeaderComponent';
import NavigationComponent from '../../components/NavigationComponent';
import LoadingComponent from '../../components/LoadingComponent';
import { upcomingMoviesAction } from '../../actions/UpcomingMoviesAction';


// The page render when first opening up the app
class UpcomingReleasesView extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            upcomingList: this.props.upcomingList,
            isLoading: true,
            currentSort: 'ReleaseDate',
            currentGenreFilter: 'None'
        }
    }
    // When the component mounts
    async componentDidMount() {
        // Fetch a list with all upcoming Movies
        await this.props.upcomingMoviesAction();
        // Update the state
        await this.setState({upcomingList: this.releaseDateOrder(this.props.upcomingList)});
        await this.setState({isLoading: false});
    }
    // A function for alphabetically ordering the upcoming movie list
    alphabeticallyOrder (AllMovies) {
        this.setState({isLoading: true});
        AllMovies.sort((movieA, movieB) => (movieA.title < movieB.title) ? -1 : 1);
        this.setState({isLoading: false});
        return AllMovies
    }
    // A function for ordering the upcoming movie list by their release date
    releaseDateOrder(AllMovies){
        this.setState({isLoading: true});
        AllMovies.sort((movieA, movieB) => (movieA['release-dateIS'].split('-').join('') > movieB['release-dateIS'].split('-').join('') ? -1 : 1));
        this.setState({isLoading: false});
        return AllMovies;
    }
    // A function that filters the upcoming movie list with the selected genre
    async filterGenre (genreFilter) {
        if(genreFilter !== 'None') {
            // show the loading sign
            await this.setState({isLoading: true});
            // get all the movies
            const AllMovies = this.props.upcomingList;
            // Create a list with all the filtered movies
            const FilteredMovies = []
            await AllMovies.filter((movie) => {
                movie.genres.filter((genre) => {
                    if(genre['NameEN\t'] === genreFilter) {
                        FilteredMovies.push(movie);
                    }
                })
            })
            // Show the filtered movie in alphabetical order if that is selected
            if(this.state.currentSort === 'Alphabetical') {
                await this.setState({upcomingList: this.alphabeticallyOrder(FilteredMovies)});
            }
            // Show the filtered movie in release date order if that is selected
            else{
                await this.setState({upcomingList: this.releaseDateOrder(FilteredMovies)});
            }
            await this.setState({isLoading: false});
        }
        // There is no genre selected so we display all movies
        else{
            await this.setState({upcomingList: this.props.upcomingList});
        }
    }
    // Render the component
    render () {
        const {upcomingList, isLoading, currentGenreFilter, currentSort} = this.state;
        return (
            <View style={GlobalStyles.Container}>
                <HeaderComponent/>

                {isLoading ?
                    <View style={styles.MovieListWrapper}>
                        <Text style={[GlobalStyles.HeaderText, {marginBottom: 10, marginLeft: '5%',}]}>
                            Upcoming Releases:
                        </Text>
                        <LoadingComponent/>
                    </View>
                :
                    <View style={styles.MovieListWrapper}>
                        <Text style={[GlobalStyles.HeaderText, {marginBottom: 10, marginLeft: '5%',}]}>
                            Upcoming Releases:
                        </Text>

                        <View style={styles.SortButtonWrapper}>
                            <Text style={styles.SortText}>
                                Sort:
                            </Text>

                            <TouchableOpacity style={currentSort === 'ReleaseDate' ? styles.SortButtonSelected : styles.SortButtonNotSelected} onPress={() => {this.setState({upcomingList: this.releaseDateOrder(upcomingList), currentSort: 'ReleaseDate'})}}>
                                <Text style={styles.SortButtonText}>
                                    By release date
                                </Text>
                                <Text style={{fontSize: 8}}>
                                    (descending order)
                                </Text>
                            </TouchableOpacity>

                            <TouchableOpacity style={currentSort === 'Alphabetical' ? styles.SortButtonSelected : styles.SortButtonNotSelected} onPress={() => this.setState({upcomingList: this.alphabeticallyOrder(upcomingList), currentSort: 'Alphabetical'})}>
                                <Text style={styles.SortButtonText}>
                                    Alphabetically
                                </Text>
                            </TouchableOpacity>
                        </View>

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
                            {upcomingList.map((movie, index) => {
                                return(
                                    <TouchableOpacity key={movie.id + '-' + index} style={styles.SingleMovie} onPress={() => this.props.navigation.navigate('UpcomingMovieSingleView', movie)}>
                                        <View style={styles.SingleMovieInfo}>
                                            <Text style={styles.SingleMovieHeader}>
                                                {movie.title}
                                            </Text>

                                            <Text style={styles.SingleMovieText}>
                                                Release date: {movie['release-dateIS']}
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

const mapStateToProps = ({upcomingList}) => ({upcomingList});

export default connect(mapStateToProps, {upcomingMoviesAction})(UpcomingReleasesView);
//export default withNavigation(ThirdView);

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
        marginRight: '5%',
        marginVertical: '1%',
        position: 'absolute',
        right: 0,
        width: '10%',
    },
    SingleGenre: {
        fontSize: 10,
        fontStyle: 'italic',
        marginLeft: '2%',
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
    SingleMovieHeader: {
        fontSize: 12,
        fontWeight: 'bold',
    },
    SingleMovieInfo: {
        justifyContent: 'center',
        marginLeft: 10,
    },
    SingleMovieText: {
        fontSize: 12,
    },
    SortButtonSelected: {
        alignItems: 'center',
        backgroundColor: '#ffffff',
        borderRadius: 20,
        borderWidth: 2,
        height: 35,
        justifyContent: 'center',
        marginHorizontal: '5%',
        width: 115,
    },
    SortButtonNotSelected: {
        alignItems: 'center',
        backgroundColor: '#EDF8DF',
        borderRadius: 20,
        borderWidth: 1,
        height: 35,
        justifyContent: 'center',
        marginHorizontal: '2%',
        width: 115,
    },
    SortButtonText: {
        fontSize: 10,
        textAlign: 'center',
    },
    SortButtonWrapper: {
        flexDirection: 'row',
        marginBottom: 5,
        marginHorizontal: '4%',
    },
    SortText: {
        fontSize: 16,
        marginTop: '2%',
        marginHorizontal: '5%',
    },
})
