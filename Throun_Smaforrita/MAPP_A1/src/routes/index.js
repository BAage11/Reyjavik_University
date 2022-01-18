import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import AddNewBoardView from '../views/BoardViews/AddNewBoardView';
import AddNewListView from '../views/ListViews/AddNewListView';
import AddNewTaskView from '../views/TaskViews/AddNewTaskView';
import ImageGalleryView from '../views/BoardViews/ImageGalleryView';
import BoardListView from '../views/BoardViews/BoardListView';
import ListView from '../views/ListViews/ListView';
import MainView from '../views/TheMainView/MainView';
import ModifyBoardView from '../views/BoardViews/ModifyBoardView';
import ModifyListColourView from '../views/ListViews/ModifyListColourView';
import ModifyListView from '../views/ListViews/ModifyListView';
import ModifyTaskView from '../views/TaskViews/ModifyTaskView';
import MoveTaskView from '../views/TaskViews/MoveTaskView';
import SingleBoardView from '../views/BoardViews/SingleBoardView';
import SingleTaskView from '../views/TaskViews/SingleTaskView';

// import all the views we nedd and add them to the stack navigator for naviagtion around the app
const StackNavigator = createStackNavigator(
    { MainView, BoardListView, ImageGalleryView, AddNewBoardView, ModifyBoardView, SingleBoardView, ListView, AddNewListView, ModifyListView, ModifyListColourView, SingleTaskView, ModifyTaskView, AddNewTaskView, MoveTaskView}
);

const AppContainer = createAppContainer(StackNavigator);

export default AppContainer;
