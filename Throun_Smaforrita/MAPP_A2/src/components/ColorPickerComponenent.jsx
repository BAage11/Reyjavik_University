import React from 'react'
import {colorList} from '../styles/GlobalStyles';
import { View, StyleSheet, Text, ScrollView, TouchableOpacity, TextInput, Alert } from 'react-native';
import { withNavigation } from 'react-navigation';
import GlobalStyles from '../styles/GlobalStyles';


// This is a scrollview component where a user is able to tap on a color to change the color of each contact
class ColorPickerComponent extends React.Component {
    constructor(props) {
        super(props);
    }
    // Render the component
    render() {
            return(
                <View>
                    <ScrollView style={styles.ColorPicker}>
                        {colorList.map((color) => {
                            return(
                                <TouchableOpacity key={color} style={[styles.ColorItem, {backgroundColor: color}]} onPress={() => {this.props.changeColor(color); this.props.closeColorPicker()}}>
                                    <Text style={styles.ColorItemText}>
                                        Tap to set this color
                                    </Text>
                                </TouchableOpacity>
                            );
                        })}
                    </ScrollView>
                    <TouchableOpacity style={GlobalStyles.Button} onPress={() => this.props.closeColorPicker()}>
                        <Text style={GlobalStyles.ButtonText}>
                            Close
                        </Text>
                    </TouchableOpacity>
                </View>
            )
        }
    }

export default withNavigation(ColorPickerComponent);

const styles = StyleSheet.create({
    ColorPicker: {
        marginVertical: 50,
        width: 300,
    },
    ColorItem: {
        alignItems: 'center',
        height: 50,
        marginVertical: 5,
        padding: 10,
    },
    ColorItemText: {
        fontSize: 16,
        fontWeight: 'bold',
        marginTop: 7,
    },
    CloseButton: {
        backgroundColor: '#ffffff',
        height: 50,
        width: 150,
        marginHorizontal: '20%',
        alignItems: 'center',
        borderWidth: 3,
    }
})
