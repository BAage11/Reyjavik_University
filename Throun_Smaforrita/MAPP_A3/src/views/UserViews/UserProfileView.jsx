import React from 'react';
import { Alert, Image, ScrollView, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { connect } from 'react-redux';
import GlobalStyles from '../../styles/GlobalStyles';
import HeaderComponent from '../../components/HeaderComponent';
import NavigationComponent from '../../components/NavigationComponent';
import RatingComponent from '../../components/RatingComponent';
import { watchListAction } from '../../actions/WatchListAction';
import {favoritesAction } from '../../actions/FavoritesAction';
import {removeMovieFromList} from '../../services/AddOrRemoveFromListServices/RemoveFromList';
import {addToMovieList} from '../../services/AddOrRemoveFromListServices/AddMovieToList';

// The page render when first opening up the app
class UserProfileView extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            isModalOpen: false,
            watchList: this.props.watchList,
            favorites: this.props.favoritesList,
            isRatingOpen: false,
            movieForRating: {},
        }
    }
    async componentDidMount() {
        await this.setState({watchList: this.alphabeticallyOrder(this.props.watchList)});
        await this.setState({favorites: this.alphabeticallyOrder(this.props.favoritesList)});
    }
    openModal() {
        this.setState({isModalOpen: true})
    }
    closeModal() {
        this.setState({isModalOpen: false})
    }

    alphabeticallyOrder (AllMovies) {

        AllMovies.sort((movieA, movieB) => (movieA.title < movieB.title) ? -1 : 1);
        return AllMovies
    }

    async addMovieToFavorites(movie) {
        const favorites = this.props.favoritesList;
        const oldLengthOfList = favorites.length;
        const newFavorites = await addToMovieList(favorites, movie);
        const newLengthOfList = newFavorites.length;
        if (oldLengthOfList < newLengthOfList){
            await this.props.favoritesAction(newFavorites);
            await this.setState({favorites: this.alphabeticallyOrder(this.props.favoritesList)});
        }
        else{
            Alert.alert(
                'Movie already in your Favorites',
            )
        }
    }

    async removeFromWatchList(movie) {
        const watchList = this.props.watchList;
        const newWatchList = await removeMovieFromList(watchList, movie);
        await this.props.watchListAction(newWatchList);
        await this.setState({watchList: this.alphabeticallyOrder(this.props.watchList)});
    }

    async removeFromFavorites(movie) {
        const favorites = this.props.favoritesList;
        const newFavorites = await removeMovieFromList(favorites, movie);
        await this.props.favoritesAction(newFavorites);
        await this.setState({favorites: this.alphabeticallyOrder(this.props.favoritesList)});
    }

    addToFavoritesOrRemoveCheck(movie) {
        const title = movie.title
        Alert.alert(
            'Removing "' + title  + '" from Watch List',
            'Do you want to add it to your Favorites or remove it?',
            [
                {
                    text: 'Move to your Favorites',
                    onPress: () => {this.addMovieToFavorites(movie); this.removeFromWatchList(movie)},
                },
                {
                  text: 'Remove from Watch List',
                  onPress: () => this.removeFromWatchList(movie),
                },
                {
                  text: 'Cancel',
                  style: 'cancel',
                },
            ],
            { cancelable: true },
        )
    }

    async addRatingToFavoriteMovie(movie, rating) {
        await this.setState({movieForRating: movie});

        await this.setState({
            movieForRating: {
                ...this.state.movieForRating,
                ['yourPersonalRating']: rating
            }

        });
        await this.removeFromFavorites(movie);
        await this.addMovieToFavorites(this.state.movieForRating);
    }

    removeFromFavoritesOrAddRatingCheck(movie) {
        Alert.alert(
            'Actions',
            'What do you want to do?',
            [
                {
                  text: 'Add your personal rating',
                  onPress: () => {this.setState({movieForRating: movie}) ; this.openRatingModal()},
                },
                {
                    text: 'Remove from Favorites',
                    onPress: () => this.removeFromFavorites(movie),
                },
                {
                  text: 'Cancel',
                  style: 'cancel',
                },
            ],
            { cancelable: true },
        )
    }

    openRatingModal() {
        this.setState({isRatingOpen: true});
    }

    closeRatingModal() {
        this.setState({isRatingOpen: false});
    }

    render () {
        const {watchList, favorites, isRatingOpen, movieForRating} = this.state;
        return (
            <View style={GlobalStyles.Container}>
                <HeaderComponent/>
                <RatingComponent isRatingOpen={isRatingOpen} closeRatingModal={this.closeRatingModal.bind(this)} addRatingToFavoriteMovie={this.addRatingToFavoriteMovie.bind(this)} movieForRating={movieForRating}/>

                <View style={styles.FavouritesWrapper}>
                    <Text style={GlobalStyles.HeaderText}>
                        Your Favorites
                    </Text>

                    <ScrollView>
                    {favorites && favorites.length > 0 ?

                        <View style={styles.WatchListMovieWrapper}>
                        <Text style={{fontSize: 8}}>
                            Tap the movies to add ratings or remove from the list
                        </Text>
                            {favorites.map((movie, index) => {
                                return (
                                    <TouchableOpacity style={styles.WatchListMovie} key={'Favorites-' + movie.title + '-' + index} onPress={() => this.removeFromFavoritesOrAddRatingCheck(movie)}>
                                        <View style={styles.SingleMovieInfo}>
                                            <Text style={styles.SingleMovieHeader}>
                                                {movie.title}
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
                                            {movie.yourPersonalRating ?
                                                <Text style={styles.SingleMovieText}>
                                                    Your rating: {movie.yourPersonalRating}
                                                </Text>
                                            :
                                                <Text style={styles.SingleMovieText}>
                                                    Your rating:
                                                </Text>
                                            }
                                        </View>
                                        <Image source={{uri: movie.poster}} style={styles.MoviePoster}/>
                                    </TouchableOpacity>
                                );
                            })}
                        </View>
                    :
                        <View style={styles.WatchListMovieWrapper}>
                            <Text>
                                {'\n'}
                                Your Favorites list is currently empty
                            </Text>
                            <Text>
                            {'\n'}
                                Your can add movies to your favorites list from your watch list after you have watched the movies
                            </Text>
                        </View>
                    }
                    </ScrollView>
                </View>
                <View style={styles.WatchListWrapper}>
                    <Text style={GlobalStyles.HeaderText}>
                        Your Watch List
                    </Text>


                    <ScrollView>
                        {watchList && watchList.length > 0 ?
                            <View style={styles.WatchListMovieWrapper}>
                                <Text style={{fontSize: 8}}>
                                    Tap the movies to move them to your Favorites or remove them
                                </Text>
                                    {watchList.map((movie, index) => {
                                        return (
                                            <TouchableOpacity style={styles.WatchListMovie} key={'WatchList-' + movie.title + '-' + index} onPress={() => this.addToFavoritesOrRemoveCheck(movie)}>
                                                <View style={styles.SingleMovieInfo}>
                                                    <Text style={styles.SingleMovieHeader}>
                                                        {movie.title}
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
                            </View>
                        :
                            <View style={styles.WatchListMovieWrapper}>
                                <Text>
                                    {'\n'}
                                    Your Watch List is currently empty!
                                </Text>
                                <Text>
                                {'\n'}
                                    Your can add movies to your personal Watch List from every movie detail screen within the app :)
                                </Text>
                            </View>
                        }
                    </ScrollView>
                </View>
            <NavigationComponent/>
            </View>
        );
    }
}

const mapStateToProps = ({favoritesList, watchList}) => ({favoritesList, watchList});

export default connect(mapStateToProps, {watchListAction, favoritesAction})(UserProfileView);

const styles = StyleSheet.create({
    FavouriteMovie: {
        backgroundColor: '#ffffff',
        height: 80,
        marginHorizontal: '5%',
        marginVertical: '2%',
        width: '90%',
    },
    FavouriteMovieWrapper: {
        height: '100%',
    },
    FavouritesWrapper: {
        borderWidth: 0.2,
        height: '35%',
        marginBottom: '5%',
        marginTop: '5%',
        width: '95%',
    },
    Genres: {
        flexDirection: 'row',
        marginLeft: '5%',
        marginVertical: '1%'
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
    WatchListMovie: {
        backgroundColor: '#ffffff',
        borderRadius: 15,
        borderWidth: 2,
        height: 70,
        marginHorizontal: '5%',
        marginVertical: '2%',
        width: '90%',
    },
    WatchListMovieWrapper: {
        height: '100%',

    },
    WatchListWrapper: {
        borderWidth: 0.2,
        height: '35%',
        marginBottom: '5%',
        marginTop: '5%',
        width: '95%',
    },
})
