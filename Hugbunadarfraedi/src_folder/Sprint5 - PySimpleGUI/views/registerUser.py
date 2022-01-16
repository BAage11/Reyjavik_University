import PySimpleGUI as sg
from views.misc.base_view import GuiWindow

class Register(GuiWindow):
    def show_window(self):
        sg.ChangeLookAndFeel('GreenTan') 

        layout = [  [sg.Text('Register')],
                    [sg.Text("*Name:",size=(8,0)), sg.Input(key='_NAME_')],
                    [sg.Text("*Email:",size=(8,0)), sg.Input(key='_EMAIL_')], 
                    [sg.Text("*Username:",size=(8,0)), sg.Input(key='_USERNAME_')], 
                    [sg.Text("*Password:",size=(8,0)), sg.Input(key='_PASSWORD_')], 
                    [sg.Text("* Must be filled")],
                    [sg.Text("", key='_error_', visible=False, size=(30, 0))],
                    [sg.Button("Register"), sg.Button("Go to log in page")]]

        window = sg.Window('Registration', layout)

        while True:

            event, values = window.Read()

            # Check what operation must be done according to the user
            if event == "Register":
            
                # Makes sure that the error message is invisable until it is needed
                window.Element('_error_').Update(visible=False)

                # Get input values
                name = values["_NAME_"]
                email = values["_EMAIL_"]
                username = values["_USERNAME_"]
                password = values["_PASSWORD_"]

                if name == "" or email == "" or username == "" or password == "":
                    # Displays the error message
                    window.Element('_error_').Update('Must fill the boxes with * in front of it.')
                    window.Element('_error_').Update(visible=True)
                else:
                    # Calls the server and registers a new user, if it returns "Error" then the email
                    # already exists
                    reg = self.actions.register_user(name, email, username, password)

                    if reg == "Error":
                        print("Email is already in use")
                    else:
                        sg.popup("Registration succesful for\nUsername: " + values["_USERNAME_"], "You can now log in from the login page.")
                        self.switch_windows(window, Login(None))

            if event == "Go to log in page":
                self.switch_windows(window, Login(self.user))
                break

            # Quits the program (X on the top right)
            if event == None or event == 'Close':
                self.hard_exit()

# It's important to keep this import at the bottom to avoid circular dependency
from views.login import Login