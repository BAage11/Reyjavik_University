import React from 'react';
import { withNavigation } from 'react-navigation';
import ModifyContactComponent from '../../components/ModifyContactComponent';

// The page rendered when wanting to modify an existin contact
class ModifyContactView extends React.Component {
    constructor(props){
        super(props);
    };
    // updating the contact list -- the update function is connected to the ContactLidtView
    async loadUpdates() {
        await this.props.navigation.state.params.loadContactUpdates();
    }
    // render the page
    render() {
        return(
            <ModifyContactComponent
                contactName={this.props.navigation.state.params.contactName}
                contactPhoneNumber={this.props.navigation.state.params.contactPhoneNumber}
                contactPhoto={this.props.navigation.state.params.contactPhoto}
                contactUUID={this.props.navigation.state.params.contactUUID}
                constactColor={this.props.navigation.state.params.contactColor}
                loadContactUpdates={this.loadUpdates.bind(this)}
                uniquePhoneNumbers={this.props.navigation.state.params.uniquePhoneNumbers}
            >
            </ModifyContactComponent>
        );
    }
}

export default withNavigation(ModifyContactView);
