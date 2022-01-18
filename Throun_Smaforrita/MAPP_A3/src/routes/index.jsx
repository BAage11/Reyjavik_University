import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import CinemasView from '../views/CinemaViews/CinemasView';
import CinemaSingleView from '../views/CinemaViews/CinemaSingleView';
import MovieSingleView from '../views/CinemaViews/MovieSingleView';
import MovieListView from '../views/CurrentlyPlayingMovieViews/MovieListView';
import CurrentlyPlayingMovieSingleView from '../views/CurrentlyPlayingMovieViews/CurrentlyPlayingMovieSingleView';
import UpcomingReleasesView from '../views//UpcomingMovieViews/UpcomingReleasesView';
import UpcomingMovieSingleView from '../views/UpcomingMovieViews/UpcomingMovieSingleView';
import UserProfileView from '../views/UserViews/UserProfileView';
import IntroView from '../views/IntroViews/IntroView';

// Create the stack navigations through the app
const StackNavigator = createStackNavigator({
    IntroView: {
        screen: IntroView,
        navigationOptions: () => ({
            title: 'Dr. Cinema',
            headerLeft: () => null,
        }),
    },
    CinemasView: {
        screen: CinemasView,
        navigationOptions: () => ({
            title: 'Cinemas',
            headerLeft: () => null,
        }),
    },
    CinemaSingleView:{
        screen: CinemaSingleView,
        navigationOptions: () => ({
            title: 'Cinema Details',
        }),
    },
    MovieSingleView: {
        screen: MovieSingleView,
        navigationOptions: () => ({
            title: 'Movie Details',
        }),
    },
    MovieListView: {
        screen: MovieListView,
        navigationOptions: () => ({
            title: 'Movies',
        }),
    },
    CurrentlyPlayingMovieSingleView: {
        screen: CurrentlyPlayingMovieSingleView,
        navigationOptions: () => ({
            title: 'Movie Details',
        }),
    },
    UpcomingReleasesView: {
        screen: UpcomingReleasesView,
        navigationOptions: () => ({
            title: 'Upcoming Releases',
        }),
    },
    UpcomingMovieSingleView: {
        screen: UpcomingMovieSingleView,
        navigationOptions: () => ({
            title: 'Upcoming Movie Details',
        }),
    },
    UserProfileView: {
        screen: UserProfileView,
        navigationOptions: () => ({
            title: 'User Profile',
        }),
    },
});



const AppContainer = createAppContainer(StackNavigator);

export default AppContainer;
