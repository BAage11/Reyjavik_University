import { getAccessToken } from '../AuthenticationServices/GetAccessToken';
import * as Endpoints from '../../constants/Endpoints';


// A function for fetching all movies playing in Iceland at the moment
export const getAllMovies = async () => {
    // Get updated token
    var accessToken = await getAccessToken();
    // Fetch the movies listed
    return fetch(Endpoints.MOVIES_ENDPOINT, {
        method: 'GET',
        headers:{
            'x-access-token': accessToken,
            'Accept': 'application/json',
            'Content-Type': 'application/json',
         }
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
            getAllMovies();
        }
    });
}
