import * as constants from '../constants/';

// update the watch list within the redux store
export default function watchListReducer (state = [], action) {
    switch (action.type) {
        case constants.GET_WATCH_LIST:
            return action.payload;
        default: return state;
    }
}
