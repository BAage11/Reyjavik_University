import * as constants from '../constants';
import { getAllMovies } from '../services/CinemaServices/GetMovies';

// The action activates on the type GET_MOVIE_LIST,
// it retreives a list of all movie and returns the list as a json object
export const getMovieListAction = () => {
    return async dispatch => {
        const movieList = await getAllMovies();
        dispatch(loadMoviesSuccess(movieList));
    }
}

const loadMoviesSuccess = movieList => ({
    type: constants.GET_MOVIE_LIST,
    payload: movieList,
});
