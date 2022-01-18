import * as Endpoints from '../../constants/Endpoints';
import { getAccessToken } from '../AuthenticationServices/GetAccessToken';

// A function for fetching the list of all cinemas in Iceland 
export const getCinemaList = async () => {
    const accessToken = await getAccessToken()
    return fetch(Endpoints.CINEMAS_ENDPOINT, {
        method: 'GET',
        headers: {
            'x-access-token': accessToken,
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
    }).then((response) => {
        // find the content type of the response,
        const contentType = response.headers.get("content-type");
        // check if it is JSON and return if so
        if (contentType && contentType.indexOf("application/json") !== -1) {
            return response.json().then((responseData) => {
                return responseData;
            })
        }
        // run the function again if not json the first time
        else {
            getCinemaList();
        }
    });
}
