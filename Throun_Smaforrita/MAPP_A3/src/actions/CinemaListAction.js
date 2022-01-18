import * as constants from '../constants/';
import { getCinemaList } from '../services/CinemaServices/GetCinemas';


// The action activates on the type GET_CINEMAS_LIST, 
// it retreives a list of all cinemas and returns the list as a json object
export const getCinemaListAction = () => {
    return async dispatch => {
        const cinemaList = await getCinemaList();
        dispatch(loadCinemasSuccess(cinemaList));
    }
};

const loadCinemasSuccess = cinemaList => ({
    type: constants.GET_CINEMAS_LIST,
    payload: cinemaList,
});
