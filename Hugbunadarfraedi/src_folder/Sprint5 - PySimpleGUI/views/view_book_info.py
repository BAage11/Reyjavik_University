import PySimpleGUI as sg
from views.misc.base_view import GuiWindow

class ViewBookInfo(GuiWindow):

    """
    The init function needs an extra parameter 'book' since user has
    selected this book to view.
    """
    def __init__(self, user, book):
        super().__init__(user)
        self.book = book

    def show_window(self):
        sg.ChangeLookAndFeel('GreenTan') 

        book_name = self.book["name"]
        author = self.book["author"][0]
        genre = self.book["genre"][0]
        published = self.book["published"]
        edition = self.book["edition"]
        condition = self.book["condition"]
                
        layout = [  [sg.Text('Detailed book information')],
                    [sg.Text("Name:",size=(8,0)), sg.Text(book_name)],
                    [sg.Text("Author:",size=(8,0)), sg.Text(author)], 
                    [sg.Text("Genre:",size=(8,0)), sg.Text(genre)], 
                    [sg.Text("Published:",size=(8,0)), sg.Text(published)], 
                    [sg.Text("Edition:",size=(8,0)), sg.Text(edition)], 
                    [sg.Text("Condition:",size=(8,0)), sg.Text(condition)], 
                    # [sg.Text("Available:"), sg.Text(available)],
                    [sg.Button("Rent book"), sg.Button("Exchange books"), sg.Button("Go Back")]]
            


        Window = sg.Window('Book information', layout)
        while True:
                event, values = Window.read()
                if event == 'Rent book':
                    # Check if book is available in database. If so, mark book as unavailable in database
                    sg.popup("The book '" + book_name + "' is confirmed for rent.\nPlease return book within 14 days.\n", title="Book Rent Confirmed", keep_on_top=True, button_color=("white", "green"))
                    # If book not available, return a message to user:
                    # sg.popup("Book selected is currently unavailable.\nPlease try again at a later stage, or select another book to rent/exchange.")
                if event == 'Exchange books':
                    self.switch_windows(Window, ExchangeBooks(self.user, self.book))
                else:
                    self.switch_windows(Window, AllBookListings(self.user))

from views.exchange_books import ExchangeBooks
from views.all_book_listings import AllBookListings
