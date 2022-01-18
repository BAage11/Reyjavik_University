import * as constants from '../constants/';

// update the watchlist within the redux store
export const watchListAction = (WatchList) => ({
    type: constants.GET_WATCH_LIST,
    payload: WatchList,
})
