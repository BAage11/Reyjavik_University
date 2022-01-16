import PySimpleGUI as sg
from views.misc.base_view import GuiWindow

"""
Login() contains the view and the functionality of logging in a user
"""
class Login(GuiWindow):

    def show_window(self):
        sg.ChangeLookAndFeel('GreenTan') 

        layout = [[sg.Text('Username: ', size=(8, 1)), sg.InputText(key="Username")],
                [sg.Text('Password: ', size=(8, 1)), sg.InputText('', key='Password', password_char='*')],
                [sg.Submit('Log in'), sg.Button('Register new account')]]
        
        Window = sg.Window('Log in', layout)
        while True:
            event, values = Window.read()
            if event == 'Cancel' or event == None:
                self.hard_exit()
            elif event == 'Register new account':
                self.switch_windows(Window, Register(self.user))
            elif values["Username"] == "" or values["Password"] == "":
                sg.popup("Missing username and/or password.\nPlease try again.", title="Missing values", keep_on_top=True, button_color=("white", "green"))
            else:
                username = values["Username"]
                password = values["Password"]
                # self.actions.login_user calls the server with the provided parameters and returns
                # and the session id if the user provides the correct information
                success = self.actions.login_user(username, password)
                if success != "":
                    # Store the user's id in self.user
                    self.user = success
                    self.switch_windows(Window, AllBookListings(self.user))
                else:
                    sg.popup("Username and/or password is wrong.\nPlease try again.")

                # print('Username:', values["Username"], 'Password:', values["Password"])

# It's important to keep this import at the bottom to avoid circular dependency
from views.registerUser import Register
from views.all_book_listings import AllBookListings