import PySimpleGUI as sg
from views.misc.base_view import GuiWindow

class UserProfile(GuiWindow):

    def show_window(self):
        # Get the user id since get_all_user_books() will use it
        self.u_id = self.actions.get_user_id_from_session(self.user)
        user_books = self.get_all_user_books()
        # Set the theme for the window
        sg.ChangeLookAndFeel('GreenTan')

        # Table nr 1. that contains all of the user's previously rented books
        # TODO: Not implemented
        table_header = ("Book name", "Author", "Genre", "Condition")
        table_values = [ ["No rented books", " ", " ", " "] ]
        table_object = sg.Table(values=table_values, headings=table_header, auto_size_columns=True, select_mode=sg.TABLE_SELECT_MODE_NONE, background_color='#d8e2de' ,alternating_row_color='#ebf0ee')

        # Make sure to have some data in the dable in case there are no books
        user_rentals = []
        if user_books == []:
            user_rentals = [ ["No books", ""] ]
        else:
            user_rentals = self.make_user_book_list(user_books)
        
        # Table nr 2. that contains all of the books that the user has up for rentals
        table_header_2 = ("Book name", "Available")
        table_values_2 = user_rentals
        table_object_2 = sg.Table(values=table_values_2, headings=table_header_2, auto_size_columns=True, select_mode=sg.TABLE_SELECT_MODE_BROWSE, background_color='#d8e2de' ,alternating_row_color='#ebf0ee')

        # Create a frame around both of the table objects so that we can place the table title above it, also just looks cleaner
        frame_rented_books = sg.Frame("Your rented books", [
            [table_object],
        ], relief=sg.RELIEF_FLAT)

        # Make 'update selected book' button unclickable if user has no books up for rental
        btn = None
        if user_books == []:
            btn = sg.Button("Update selected book", disabled=True)
        else:
            btn = sg.Button("Update selected book")

        frame_available_books = sg.Frame("Your available books", [
            [table_object_2],
            [btn]
        ], relief=sg.RELIEF_FLAT)

        # The final layout of the window
        btn_back =              sg.Button("Back")
        btn_create_new_book =   sg.Button("Create a new book")
        btn_logout =            sg.Button("Logout", button_color=("white", "red"))
        layout = [
            [ frame_rented_books, frame_available_books],
            [ btn_back, btn_create_new_book, btn_logout ]
        ]

        # Get the username of the user to display in the title of the window
        user_info = self.actions.get_user_info(self.u_id)
        Window = sg.Window('Your profile - ' + user_info["username"], layout)
        # The window loop
        running = True
        while running:
                event, values = Window.read()
                if(event is None or event == 'Exit'):
                    self.hard_exit()
                if(event == 'Update selected book'):
                    # Make sure that some row is selected
                    if(table_object_2.SelectedRows != []):
                        row_selection = table_object_2.SelectedRows[0]
                        selected_book = user_books[row_selection]
                        self.switch_windows(Window, UpdateBook(self.user, selected_book))
                    else:
                        # Show this warning to the user if he didn't select a book before clicking the select button
                        sg.Popup("Please click on a book first before you do this action", title="Action warning", keep_on_top=True, no_titlebar=True, button_color=("white", "red"))
                if(event == 'Create a new book'):
                    self.switch_windows(Window, AddBook(self.user))
                if event == "Logout":
                    self.switch_windows(Window, Login(None))
                if(event == 'Back'):
                    self.switch_windows(Window, AllBookListings(self.user))
    
    """
    Since there is no easy way to get a book by a single user on the server side, it needs to be
    implemented here, simply go through all books in database and check if their user_id is the current
    users id
    """
    def get_all_user_books(self):
        all_books = self.actions.get_all_books()
        user_books = []
        for book in all_books:
            if all_books[book]["user_id"] == self.u_id:
                user_books.append(all_books[book])
        return user_books
    
    """
    Creates the list that the table will use
    """
    def make_user_book_list(self, books):
        return_list = []
        for book in books:
            return_list.append( [ book["name"], str(book["status"]) ] )
        return return_list
    
    """
    Gets all of the user rented books

    TODO: Not implemented
    """
    def get_all_user_rented_books(self):
        get_all_rentals = self.actions.get_all_rentals()
        user_rentals = []
        for rental in get_all_rentals:
            pass


from views.all_book_listings import AllBookListings
from views.update_book import UpdateBook
from views.login import Login
from views.add_book import AddBook