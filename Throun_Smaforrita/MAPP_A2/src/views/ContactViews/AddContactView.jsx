import React from 'react';
import { withNavigation } from 'react-navigation';
import AddContactComponent from '../../components/AddContactComponent';

// The page rendered when adding a contact to the app
class AddContactView extends React.Component {
    constructor(props){
        super(props);
    }
    // Render the page and call the AddContactComponent
    render() {
        return(
            <AddContactComponent>
            </AddContactComponent>
        );
    }
}

export default withNavigation(AddContactView);
