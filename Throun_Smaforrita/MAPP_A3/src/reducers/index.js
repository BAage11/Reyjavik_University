import { combineReducers } from 'redux';
import userInfo from './UserProfileReducers';
import cinemaList from './CinemaListReducer';
import movieList from './MovieListReducer';
import upcomingList from './UpcomingListReducer';
import watchList from './WatchListReducer';
import favoritesList from './FavoritesReducer';

// combine all reducers to use within the redux store
export default combineReducers({
    userInfo,
    cinemaList,
    movieList,
    upcomingList,
    watchList,
    favoritesList
})
