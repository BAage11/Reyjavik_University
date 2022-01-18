import { StyleSheet } from 'react-native';


// Color object for accessing the colors form within the app
export const colors = {
    periwinkle: '#CAE5FF',
    freshAir: '#ACEDFF',
    jordyBlue:'#89BBFE',
    silverLakeBlue: '#6F8AB7',
    graniteGray: '#615D6C',
    darkerBlue: '#42638E',
    lightGreen: '#93FDA8',
    darkGreen: '#3FAC55',
    beige: '#FFBFA3',
    sharpYellow: '#FFF363',
    lightPink: '#F67EB8',
    lightPurple: '#A569BD',
}

// For the color picker (ColorPickerComponent)
export const colorList = ['#6F8AB7', '#ACEDFF', '#89BBFE', '#2E86C1', '#93FDA8', '#3FAC55', '#FFBFA3', '#FFF363', '#F67EB8', '#A569BD', '#FFFFFF', '#CAE5FF', '#615D6C']

// The Global stylesheet used within the app
const GlobalStyles = StyleSheet.create({
    Button: {
        alignItems: 'center',
        backgroundColor: '#ffffff',
        borderColor: '#2E86C1',
        borderRadius: 40,
        borderWidth: 4,
        height: 55,
        marginVertical: '5%',
        width: 280,
    },
    ButtonText: {
      alignContent: 'center',
      color: '#000000',
      fontSize: 16,
      fontWeight: 'bold',
      marginVertical: '5%',
      textAlign: 'center',
    },
    Container: {
        alignItems: 'center',
        backgroundColor: '#EDF8DF',
        borderColor: '#ffffff',
        borderWidth: 0.2,
        flex: 1,
    },
    HeaderText: {
        fontSize: 18,
        fontWeight: 'bold',
    },
    NormalText: {
        fontSize: 15,
    },
    TextInput: {
        backgroundColor: '#ffffff',
		borderWidth: 1.5,
		height: 50,
		marginBottom: '2%',
		marginLeft: 30,
		marginRight: 30,
		marginVertical: '5%',
        paddingLeft: 10,
		textAlign: "left",
        width: 300,
	},
});

export default GlobalStyles;
