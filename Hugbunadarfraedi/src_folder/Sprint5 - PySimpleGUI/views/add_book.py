import PySimpleGUI as sg
from views.misc.base_view import GuiWindow

class AddBook(GuiWindow):

    def show_window(self):

        sg.ChangeLookAndFeel('GreenTan') 
    
        layout = [  [sg.Text('Register New Book')],
                    [sg.Text("*Name:",size=(8,0)), sg.Input(key='_NAME_')],
                    [sg.Text("*Author:",size=(8,0)), sg.Input(key='_AUTHOR_')], 
                    [sg.Text("*Genres:",size=(8,0)), sg.Input(key='_GENRES_')], 
                    [sg.Text(" Published:",size=(8,0)), sg.Input(key='_PUBLISHED_')], 
                    [sg.Text(" Edition:",size=(8,0)), sg.Input(key='_EDITION_')], 
                    [sg.Text("*Condition:",size=(8,0)), sg.Drop(['Good', 'Mediocre', 'Bad'], readonly=True, key='_CONDITION_')], 
                    [sg.Text("* Must be filled")],
                    [sg.Text("", key='_error_', visible=False, size=(30, 0))],
                    [sg.Button("Create Book"), sg.Button("Back")]]

        window = sg.Window('Booking', layout)

        while True:
            # Get the input from user
            event, values = window.Read()

            # Check what operation must be done according to the user
            if event == "Create Book":
                """ TO DO create book """
                # Makes sure that the error message is invisable until it is needed
                window.Element('_error_').Update(visible=False)
                # Check if the user has entered the bare mininum
                if values['_NAME_'] == '' or values['_AUTHOR_'] == '' or values['_GENRES_'] == '' or values['_CONDITION_'] == '':
                    # Displays the error message
                    window.Element('_error_').Update('Must fill the boxes with * in front of it.')
                    window.Element('_error_').Update(visible=True)
                else:
                    # Converts the condition to numeric value
                    con = 0
                    if(values['_CONDITION_'] == 'Good'):
                        con = 3
                    elif(values['_CONDITION_'] == 'Mediocre'):
                        con = 2
                    else:
                        con = 1
                    
                    bookname = values["_NAME_"]
                    author = [values["_AUTHOR_"]]
                    genre = [values["_GENRES_"]]
                    published = values["_PUBLISHED_"]
                    edition = values["_EDITION_"]
                    condition = con

                    u_id = self.actions.get_user_id_from_session(self.user)
                    print(self.actions.add_book(u_id, bookname, author, genre, published, edition, condition))
                    sg.popup("Book has hereby been registered as follows:", "Name: " + values["_NAME_"], "Author: " + values["_AUTHOR_"], "Genre: " + values["_GENRES_"], "Published: " + values["_PUBLISHED_"], "Edition: " + values["_EDITION_"], "Condition:" + values["_CONDITION_"])
 
                    self.switch_windows(window, UserProfile(self.user))
 
            # Goes to the profile page
            if event == "Back":
                self.switch_windows(window, UserProfile(self.user))

            # Quits the program (X on the top right)
            if event == None:
                break

        window.Close()

from views.user_profile import UserProfile