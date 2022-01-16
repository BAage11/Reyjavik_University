import PySimpleGUI as sg
from views.misc.base_view import GuiWindow

class AllBookListings(GuiWindow):

    def show_window(self):
        books, books_dict = self.get_books()

        sg.ChangeLookAndFeel('GreenTan')

        # Table for all the books in the system
        table_header = ("Name", "Author", "Genre", "Condition")
        #table_values = self.make_fake_values(40)
        table_values = books
        table = sg.Table(values=table_values, headings=table_header, select_mode=sg.TABLE_SELECT_MODE_BROWSE,
             background_color='#d8e2de' ,alternating_row_color='#ebf0ee', num_rows=15)

        # Put a frame around the table
        frame_all_books = sg.Frame("All books", [[table]], relief=sg.RELIEF_FLAT)

        # Final layout of the window
        layout = [
            [ frame_all_books ],
            [ sg.Button("More Info"), sg.Button("My profile")]
        ]

        window = sg.Window('Book listings', layout)
        while True:
            event, values = window.read()

            if event == "My profile":
                self.switch_windows(window, UserProfile(self.user))
            elif event == "More Info":
                # Make sure that a row has been selected in the table
                if(table.SelectedRows != []):
                    row_selection = table.SelectedRows[0]
                    selected_book = books_dict[table.Values[row_selection][0]]
                    self.switch_windows(window, ViewBookInfo(self.user, selected_book))
                else:
                    sg.Popup("Please click on a book first before you do this action", title="Action warning", keep_on_top=True, no_titlebar=True, button_color=("white", "red"))
            elif event == None:
                self.hard_exit()
    
    """
    get_condition() takes a number from 1-3 as an argument and returns the
    state of the book
    """
    def get_condition(self, number):
        if number % 3 == 0:
            return "Bad"
        elif number % 3 == 1:
            return "Mediocre"
        else:
            return "Good"
    
    """
    Temporary function that creates fakes values for the table, just for looks.
    """
    def make_fake_values(self, nr_of_rows):
        return_arr = [ ]
        for x in range(0, nr_of_rows):
            book_name = "Book " + str(x + 1)
            author_name = "Author " + str(x + 1)
            genre_info = "Genre " + str(x + 1)
            condition = self.get_condition(x + 1)
            return_arr.append([book_name, author_name, genre_info, condition])
        return return_arr
    
    def get_books(self):
        books = self.actions.get_all_books()
        
        return_books = []
        book_dict = {}

        for key, book in books.items():
            book_name = book['name']

            if(book['status'] != 1):
                continue
            
            if('author' in book):
                author_name = book['author']
            elif('authors' in book):
                author_name = book['authors']

            if('genre' in book):
                genre_info = book['genre']
            elif('genres' in book):
                genre_info = book['genres']
            
            if('edition' in book):
                edition_info = book['edition']
            else:
                edition_info = 'NaN' 

            if('book_id' in book):
                book_id = book['book_id']
            elif('id' in book):
                book_id = book['id']

            condition = self.get_condition(book['condition'])

            book_dict[book_name] = {'name': book_name, 'author': author_name, 'genre': genre_info, 'published': book['published'], 'edition': edition_info, 'condition': condition, 'id': book_id}
            return_books.append([book_name, author_name, genre_info, condition])

        return return_books, book_dict

from views.user_profile import UserProfile
from views.view_book_info import ViewBookInfo