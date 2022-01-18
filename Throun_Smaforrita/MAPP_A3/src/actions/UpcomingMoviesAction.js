import * as constants from '../constants/';
import { getUpcomingMovies } from '../services/CinemaServices/GetUpcomingMovies';


// The action activates on the type GET_CINEMAS_LIST, 
// it retreives a list of all cinemas and returns the list as a json object
export const upcomingMoviesAction = () => {
    return async dispatch => {
        const upcomingList = await getUpcomingMovies();
        dispatch(loadUpcomingSuccess(upcomingList));
    }
};

const loadUpcomingSuccess = upcomingList => ({
    type: constants.GET_UPCOMING,
    payload: upcomingList,
});
