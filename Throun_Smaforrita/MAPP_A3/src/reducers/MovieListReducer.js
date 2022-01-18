import * as constants from '../constants/';

// update the movie list within the redux store
export default function moviesListReducer (state = [], action) {
    switch (action.type) {
        case constants.GET_MOVIE_LIST:
            return action.payload;
        default: return state;
    }
}
