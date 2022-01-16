import PySimpleGUI as sg
from views.misc.base_view import GuiWindow

class UpdateBook(GuiWindow):

    def __init__(self, user, book):
        super().__init__(user)
        self.book = book

    def show_window(self):
        
        sg.ChangeLookAndFeel('GreenTan') 

        condition = self.convert_condition(self.book["condition"])

        layout = [  [sg.Text('Update book')],
                    [sg.Text("*Name:",size=(8,0)), sg.Input(key='_NAME_', default_text=self.book["name"])],
                    [sg.Text("*Author:",size=(8,0)), sg.Input(key='_AUTHOR_', default_text=self.book["authors"][0])], 
                    [sg.Text("*Genres:",size=(8,0)), sg.Input(key='_GENRES_', default_text=self.book["genres"][0])], 
                    [sg.Text(" Published:",size=(8,0)), sg.Input(key='_PUBLISHED_', default_text=self.book["published"])], 
                    [sg.Text(" Edition:",size=(8,0)), sg.Input(key='_EDITION_', default_text=self.book["edition"])], 
                    [sg.Text("*Condition:",size=(8,0)), sg.Drop(['Good', 'Mediocre', 'Bad'], default_value=condition, readonly=True, key='_CONDITION_')], 
                    [sg.Text("* Must be filled")],
                    [sg.Text("", key='_error_', visible=False, size=(30, 0))],
                    [sg.Button("Update book"), sg.Button("Back")]]

        window = sg.Window('Booking', layout)

        while True:
            # Get the input from user
            event, values = window.Read()

            # Check what operation must be done according to the user
            if event == "Update book":
                # Makes sure that the error message is invisable until it is needed
                window.Element('_error_').Update(visible=False)
                # Check if the user has entered the bare mininum
                if values['_NAME_'] == '' or values['_AUTHOR_'] == '' or values['_GENRES_'] == '' or values['_CONDITION_'] == '':
                    # Displays the error message
                    window.Element('_error_').Update('Must fill the boxes with * in front of it.')
                    window.Element('_error_').Update(visible=True)
                else:                    
                    updated_bookname = values["_NAME_"]
                    updated_author = [values["_AUTHOR_"]]
                    updated_genre = [values["_GENRES_"]]
                    updated_published = values["_PUBLISHED_"]
                    updated_edition = values["_EDITION_"]
                    updated_condition = self.condition_to_number(values["_CONDITION_"])

                    # Calls the server and tells it to update the book
                    self.actions.update_book(self.book["id"], self.user, 
                        updated_bookname, updated_author, updated_genre, updated_published, updated_edition, updated_condition)
                    sg.popup("Book has hereby been updated as follows:", "Name: " + values["_NAME_"], "Author: " + values["_AUTHOR_"], "Genre: " + values["_GENRES_"], "Published: " + values["_PUBLISHED_"], "Edition: " + values["_EDITION_"], "Condition:" + values["_CONDITION_"])
 
                    self.switch_windows(window, AllBookListings(self.user))
 
            # Goes to the profile page
            if event == "Back":
                self.switch_windows(window, UserProfile(self.user))
            # Quits the program (X on the top right)
            if event == None:
                self.hard_exit()

        window.Close()
    
    def condition_to_number(self, condition):
        if condition == "Bad":
            return 1
        elif condition == "Mediocre":
            return 2
        else:
            return 3

    def convert_condition(self, condition):
        if condition == 1:
            return "Bad"
        elif condition == 2:
            return "Mediocre"
        else:
            return "Bad"

from views.user_profile import UserProfile
from views.all_book_listings import AllBookListings