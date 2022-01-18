import React from 'react';
import { ScrollView, StatusBar, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { connect } from 'react-redux';
import GlobalStyles from '../../styles/GlobalStyles';
import HeaderComponent from '../../components/HeaderComponent';
import NavigationComponent from '../../components/NavigationComponent';
import LoadingComponent from '../../components/LoadingComponent';
import { getCinemaListAction } from '../../actions/CinemaListAction';
import { latinizeWord } from '../../services/LatinizeServices/Latinize';


// The page render when first opening up the app
class CinemasView extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            isLoading: true,
        }
    }
    // When the component mounts
    async componentDidMount() {
        // Get a list of all the cinemas
        await this.props.getCinemaListAction();
        // stop loading
        await this.setState({isLoading: false});
    }
    // a function for alphabetically ordering all the cinames
    alphabeticallyOrder (CinemaList) {
        CinemaList.sort((CinemaA, CinemaB) => (latinizeWord(CinemaA.name) < latinizeWord(CinemaB.name)) ? -1 : 1);
        return CinemaList
    }
    // Render the component
    render () {
        const cinemaList = this.alphabeticallyOrder(this.props.cinemaList);
        const {isLoading} = this.state;
        //const cinemaList = this.props.cinemaList;
        return (
            <View style={GlobalStyles.Container}>
                <HeaderComponent/>

                {isLoading ?
                    <View style={styles.CinemaListWrapper}>
                        <Text style={[GlobalStyles.HeaderText, {marginBottom: 10, marginLeft: '5%',}]}>
                            Cinemas:
                        </Text>

                        <LoadingComponent/>
                    </View>
                :
                    <View style={styles.CinemaListWrapper}>
                        <Text style={[GlobalStyles.HeaderText, {marginBottom: 10, marginLeft: '5%',}]}>
                            Cinemas:
                        </Text>

                        <ScrollView >
                            {cinemaList.map((cinema) => {
                                return(
                                    <TouchableOpacity key={cinema.id} style={styles.SingleCinema} onPress={() => this.props.navigation.navigate('CinemaSingleView', cinema)}>
                                        <View style={styles.SingleCinemaInfo}>
                                            <Text style={styles.SingleCinemaHeader}>
                                                {cinema.name}
                                            </Text>

                                            <Text style={styles.SingleCinemaText}>
                                                {cinema.website}
                                            </Text>
                                        </View>
                                    </TouchableOpacity>
                                );
                            })}
                        </ScrollView>
                    </View>
                }
            <NavigationComponent/>
            <StatusBar/>
            </View>
        );
    }
}

const mapStateToProps = ({cinemaList}) => ({cinemaList});

export default connect(mapStateToProps, {getCinemaListAction})(CinemasView);

const styles = StyleSheet.create({
    CinemaListWrapper: {
        height: '80%',
        marginTop: '2%',
        width: '100%',
    },
    SingleCinema: {
        backgroundColor: '#ffffff',
        borderRadius: 15,
        borderWidth: 2,
        height: 60,
        justifyContent: 'center',
        marginHorizontal: '7.5%',
        marginVertical: 5,
        width: '85%',
    },
    SingleCinemaHeader: {
        fontSize: 16,
        fontWeight: 'bold',
        textAlign: 'center',
    },
    SingleCinemaText: {
        fontSize: 14,
        textAlign: 'center',
    },
})



// {cinemaList.map((cinema) => {
//     return(
//         <TouchableOpacity key={cinema.id} style={styles.SingleCinema} onPress={() => this.props.navigation.navigate('CinemaSingleView', cinema)}>
//             <View style={styles.SingleCinemaInfo}>
//                 <Text style={styles.SingleCinemaHeader}>
//                     {cinema.name}
//                 </Text>
//
//                 <Text style={styles.SingleCinemaText}>
//                     {cinema.website}
//                 </Text>
//             </View>
//         </TouchableOpacity>
//     );
// })}
