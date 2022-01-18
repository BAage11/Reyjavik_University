import * as constants from '../constants/';

// update the users name and image within the redux store
export const changeUserInfo = (userName, userImage) => ({
    type: constants.CHANGE_USER_INFO,
    payload: {userName, userImage}
})
