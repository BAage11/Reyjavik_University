import * as constants from '../constants/';


// action for updating the favorites list within the redux store
export const favoritesAction = (FavoritesList) => ({
    type: constants.GET_FAVORITES_LIST,
    payload: FavoritesList,
})
