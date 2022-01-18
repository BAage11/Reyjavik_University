import { StyleSheet} from 'react-native';


export const base = {
    headings: {
        fontWeight: 'bold',
    },
}

export const headings = {
    h1: {
        ...base.headings,
        fontSize: 32,
    },
    h2: {
        ...base.headings,
        fontSize: 24,
    },
    h3: {
        ...base.headings,
        fontSize: 18,
    },
    h4: {
        ...base.headings,
        fontSize: 16,
    },
};

export const colors = {
    periwinkle: '#CAE5FF',
    freshAir: '#ACEDFF',
    jordyBlue:'#89BBFE',
    silverLakeBlue: '#6F8AB7',
    graniteGray: '#615D6C',
    darkerBlue: '#42638E',
}

export const colorList = ['#6F8AB7', '#ACEDFF', '#89BBFE', '#2E86C1', '#93FDA8', '#3FAC55', '#FFBFA3', '#FFF363', '#F67EB8', '#A569BD', '#FFFFFF', '#CAE5FF', '#615D6C', '#000000']


const GlobalStyles = StyleSheet.create({
    ActionButton: {
        alignItems: 'center',
        backgroundColor: '#000000',                       // 'lightgreen',
        borderColor: '#ffffff',
        borderWidth: 2,
        height: 40,
        marginVertical: 6,
        width: 180,
    },
    ButtonText: {
      alignContent: 'center',
      color: '#ffffff',
      fontSize: 16,
      fontWeight: 'bold',
      marginVertical: 7,
      textAlign: 'center',
    },
    container: {
        alignItems: 'center',
        backgroundColor: '#42638E',                   // '#feffa3',
        borderWidth: 4,
        flex: 1,
    },
});

export default GlobalStyles;
