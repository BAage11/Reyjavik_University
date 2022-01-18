import * as Endpoints from '../../constants/Endpoints';

// A function for fetching an authentication token from kvikmyndir.is
export const getAccessToken = () => {
    return fetch(Endpoints.AUTHENTICATION_ENDPOINT, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
          },
        body: JSON.stringify({
            username: 'Group5Again',
            password: 'Group5Again'
        })
    })
    .then((response) => {
        // find the content type of the response,
        const contentType = response.headers.get("content-type");
        // check if it is JSON and return if so
        if (contentType && contentType.indexOf("application/json") !== -1) {
            return response.json().then((responseData) => {
                return responseData.token;
            });
        }
        // run the function again if not json the first time
        else {
            getAccessToken();
        }
    });
};



// const tempToken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfaWQiOiI1ZmNlMzkwOTE2ZjczZjE2NjQ4OThjNzEiLCJnbG9iYWxhZG1pbiI6ZmFsc2UsImFkbWluIjpmYWxzZSwiYWN0aXZlIjp0cnVlLCJmdWxsbmFtZSI6IlJhZ25hciBHZWlyIFJhZ25hcnNzb24iLCJlbWFpbCI6InJhZ25hcnIxOEBydS5pcyIsInVzZXJuYW1lIjoicmFnZ2lyYWdnczE5OTciLCJwYXNzd29yZCI6IiQyYSQwOCRYY3Mvc0xCRUlVVFN2NUNZdElGQ0Iub2VLQ2U2bmRhcU5xLkZ3aDdHb0hGV0hvRVBwSm13MiIsImRvbWFpbiI6ImxvY2FsaG9zdDo5MDAwIiwibWVzc2FnZSI6InN0dWRlbnQgcHJvamVjdCBIUiIsImlhdCI6MTYwNzM1MzQyOSwiZXhwIjoxNjA3NDM5ODI5fQ.BMuivCEWggfUDoEmCLqzXrRbFGoeNWvwcXJ6sBffkkA'
//
// .then((response) => response.json()).then((responseData) => {
//     return responseData.token;
// });
