import React from 'react';
import { StatusBar } from 'react-native';
import { Provider, connect } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import reducers from './src/reducers';
import AppContainer from './src/routes/index';


class SubApp extends React.Component {
    render() {
        return (
            <AppContainer />
        )
    }
}

const ConnectedSubApp = connect(null, null)(SubApp);

export default function App() {
    return (
        <Provider store={createStore(reducers, applyMiddleware(thunk))}>
            <ConnectedSubApp />
            <StatusBar/>
        </Provider>
    );
}
