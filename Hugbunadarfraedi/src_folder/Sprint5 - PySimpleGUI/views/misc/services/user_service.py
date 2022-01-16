from views.misc.services.connection import Connection

class UserService(Connection):
    """
    register_user() gets all the information about a user and
    creates a dictionary that can be sent over to the server
    """
    def register_user(self, name, email, username, password):
        model = {"op": "add_user", "user_model": {
            "name": name,
            "email": email,
            "username": username,
            "password": password,
            "is_admin": False
        }}
        return self.execute(model)
    
    """
    login_user() takes in a username and pasword and returns a
    user token on success
    @return 'string' identification of the user if user successfully logs in or an empty
            string if the user fails to provide correct details.
        -NOTE: The identification is not the user's id or username, but rather a token that is used to verify him
    """
    def login_user(self, username, password):
        model = {"op": "log_in_with_username_password",
                "username": username,
                "password": password }
        return self.execute(model)
    
    """
    Returns a user id from a given session id
    @return 'string' the user's id
    """
    def get_user_id_from_session(self, session_id):
        model = {"op": "get_user_from_session_id",
                "session_id": session_id}
        return self.execute(model)
    
    """
    @return 'dict' information about the user
    """
    def get_user_info(self, user_id):
        model = {"op": "get_user_info",
                 "user_id": user_id}
        return self.execute(model)
    
    def get_all_books(self):
        model = {"op": "get_all_books"}
        return self.execute(model)