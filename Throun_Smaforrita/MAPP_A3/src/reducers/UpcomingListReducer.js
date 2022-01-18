import * as constants from '../constants/';

// update the upcoming movie list within the redux store
export default function UpcomingListReducer (state = [], action) {
    switch (action.type) {
        case constants.GET_UPCOMING: return action.payload;
        default: return state;
    }
}
