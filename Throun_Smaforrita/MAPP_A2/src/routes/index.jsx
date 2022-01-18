import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import AddContactView from '../views/ContactViews/AddContactView';
import ContactDetailsView from '../views/ContactViews/ContactDetailsView';
import ContactListView from '../views/ContactListViews/ContactListView';
import ModifyContactView from '../views/ContactViews/ModifyContactView';
import WelcomeView from '../views/WelcomeViews/WelcomeView'

// Create the stack navigations through the app
const StackNavigator = createStackNavigator({
    WelcomeView: {
        screen: WelcomeView,
        navigationOptions: () => ({
            title: 'Welcome',
        }),
    },
    ContactListView: {
        screen: ContactListView,
        navigationOptions: () => ({
            title: 'The Contactor',
            headerLeft: () => null,
        }),
    },
    AddContactView: {
        screen: AddContactView,
        navigationOptions: () => ({
            title: 'The Contactor',
        }),
    },
    ContactDetailsView: {
        screen: ContactDetailsView,
        navigationOptions: () => ({
            title: 'The Contactor',
        }),
    },
    ModifyContactView: {
        screen: ModifyContactView,
        navigationOptions: () => ({
            title: 'The Contactor',
            }),
        },
    },
    {
    defaultNavigationOptions: {
        headerTitle: "The Contactor",
        headerStyle: {
            height: 80,
        },
        headerTitleStyle: {
            fontSize: 20
        },
        headerBackTitle: "Go back",
        headerTintColor: '#000000',
    }
}
);

const AppContainer = createAppContainer(StackNavigator);

export default AppContainer;
