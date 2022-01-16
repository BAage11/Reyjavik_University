
import PySimpleGUI as sg
# Very basic window.  Return values as a list
layout = [      
          [sg.Text('Log In')],      
          [sg.Text('Id: ', size=(2, 1)), sg.InputText()],  
          [sg.Submit('Register'), sg.Cancel('Login')]      
         ]
window = sg.Window('Rent A Book Enterprice').Layout(layout)         
button, values = window.Read()


print(button, values[0])
