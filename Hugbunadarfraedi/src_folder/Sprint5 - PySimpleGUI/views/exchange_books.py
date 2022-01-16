import PySimpleGUI as sg      
from views.misc.base_view import GuiWindow

"""
ExchangeBooks() contains the view and the functionality of exchanging books between users
"""
class ExchangeBooks(GuiWindow):
        def __init__(self, user, book):
                super().__init__(user)
                self.book = book

        def show_window(self):
                sg.ChangeLookAndFeel('GreenTan')     
                self.u_id = self.actions.get_user_id_from_session(self.user)
                user_books = self.get_all_user_books()
 

                user_rentals = []
                if user_books == []:
                        user_rentals = ["-- No books registered --", ""]
                else:
                        user_rentals = self.make_user_book_list(user_books)
                
                # Get listed books of user and put into 'LISTBOX' value fields (instead of 'MyBook_1....')
                layout = [[sg.Text('Pick your book to exchange with:')],
                        [sg.Listbox(values=user_rentals, select_mode = sg.LISTBOX_SELECT_MODE_SINGLE, size = (50,5))],   
                # Get book name from earlier step and put into text field:
                        [sg.Text('Book to get instead: ' + self.book["name"], size = (50,2))],
                        [sg.Submit("Make Exchange"), sg.Cancel("Back")]]      

                Window = sg.Window('Exchange books', layout)
                while True:
                        event, values = Window.read()
                        print(values)
                        if event == 'Cancel' or event == None:
                                self.hard_exit()
                        if event == 'Back':
                                self.switch_windows(Window, ViewBookInfo(self.user, self.book))
                        if event == 'Make Exchange':
                                if values[0] == []:
                                        sg.popup("Please select a book to exchange.", title="Error!", keep_on_top=True, button_color=("white", "green"))
                                else:
                                        # If books are both available, write into database that the books are currently unavailable
                                        sg.popup("Books have hereby been exchanged.\nBook received: " + self.book["name"] + "\nBook exchanged: " + values[0][0][0])
                                        self.switch_windows(Window, AllBookListings(self.user))
                                        # else, return an error message (popup) that the books cannot be exchanged due to unavailability:
                                        # sg.popup("Book(s) selected is/are currently unavailable.\nPlease try again.")

        def get_all_user_books(self):
                all_books = self.actions.get_all_books()
                user_books = []
                for book in all_books:
                        if all_books[book]["user_id"] == self.u_id:
                                user_books.append(all_books[book])
                return user_books
    
        def make_user_book_list(self, books):
                return_list = []
                for book in books:
                        return_list.append( [ book["name"] ] )
                return return_list



from views.view_book_info import ViewBookInfo
from views.all_book_listings import AllBookListings