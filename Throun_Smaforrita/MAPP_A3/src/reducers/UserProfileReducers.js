import * as constants from '../constants/index';

// update the userInfo within the redux store
export default function changeUserInfoReducer (state={userName: '', userImage: 'https://www.techpowerusa.com/wp-content/uploads/2017/06/default-user.png'}, action) {
    switch (action.type) {
        case constants.CHANGE_USER_INFO: return action.payload;
        default: return state;
    }
}
