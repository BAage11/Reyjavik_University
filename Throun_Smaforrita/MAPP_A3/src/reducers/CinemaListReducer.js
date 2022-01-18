import * as constants from '../constants/';

// update the cinemalist within the redux store
export default function cinemaListReducer (state = [], action) {
    switch (action.type) {
        case constants.GET_CINEMAS_LIST: return action.payload;
        default: return state;
    }
}
