import json
from views.misc.services.user_service import UserService
from views.misc.services.book_service import BookService
from views.misc.services.rental_service import RentalService

class ComponentInterface():
    
    def __init__(self):
        self._user_service = UserService()
        self._book_service = BookService()
        self._rental_service = RentalService()

    # User services

    """
    Registers a new user into the system
    """
    def register_user(self, name, email, username, password):
        return self._user_service.register_user(name, email, username, password)
    
    """
    Attempts to login a user into the system
    """
    def login_user(self, username, password):
        return self._user_service.login_user(username, password)
    
    """
    Returns the user's id from a given session id
    """
    def get_user_id_from_session(self, session_id):
        return self._user_service.get_user_id_from_session(session_id)
    
    """
    Returns all information about the user from his/her's user id
    """
    def get_user_info(self, user_id):
        return self._user_service.get_user_info(user_id)
    
    # Book services

    """
    Adds a book to the system tied to a single user
    """
    def add_book(self, user_id, name, authors, genres, published, edition, condition):
        return self._book_service.add_book(user_id, name, authors, genres, published, edition, condition)

    def update_book(self, book_id, user_session, name, authors, genres, published, edition, condition):
        return self._book_service.update_book(book_id, user_session, name, authors, genres, published, edition, condition)

    def get_all_books(self):
        return self._book_service.get_all_books()
    
    # Rental services

    def get_all_rentals(self):
        return self._rental_service.get_all_rentals()