import * as constants from '../constants/';

// update the favorites within the redux store
export default function favoritesReducer (state = [], action) {
    switch (action.type) {
        case constants.GET_FAVORITES_LIST:
            return action.payload;
        default: return state;
    }
}
