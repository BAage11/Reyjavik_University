from views.misc.services.connection import Connection
import json

class BookService(Connection):
    
    def add_book(self, user_id, name, authors, genres, published, edition, condition):
        model = {"op": "add_book", "book_model": {
            "user_id": user_id,
            "name": name,
            "authors": authors,
            "genres": genres,
            "published": int(published),
            "edition": int(edition),
            "condition": int(condition)
        }}
        return self.execute(model)

    def get_all_books(self):
        model = {"op": "get_all_books"}
        return self.execute(model)
    
    # Server gives an error when this function is called, see below.
    def update_book(self, book_id, user_session, name, authors, genres, published, edition, condition):
        model = {"op": "update_book", 
                "book_id": book_id,
                "session_id": user_session,
                "book_model": {
                    "name": name,
                    "authors": authors,
                    "genres": genres,
                    "published": int(published),
                    "edition": int(edition),
                    "condition": int(condition)
                }}
        print(model)
        return self.execute(model)
    
    """
            Error in connection handler
        Traceback (most recent call last):
        File "/usr/local/lib/python3.6/dist-packages/websockets/server.py", line 195, in handler
            await self.ws_handler(self, path)
        File "/var/new-python-server/src/app/server/server.py", line 37, in __message_handler
            return_value = getattr(self.interface, data["op"])(data)
        File "/var/new-python-server/src/app/server/component_interface.py", line 44, in update_book
            return json.dumps(updated_book)
        File "/usr/lib/python3.6/json/__init__.py", line 231, in dumps
            return _default_encoder.encode(obj)
        File "/usr/lib/python3.6/json/encoder.py", line 199, in encode
            chunks = self.iterencode(o, _one_shot=True)
        File "/usr/lib/python3.6/json/encoder.py", line 257, in iterencode
            return _iterencode(o, 0)
        File "/usr/lib/python3.6/json/encoder.py", line 180, in default
            o.__class__.__name__)
        TypeError: Object of type 'ValueError' is not JSON serializable


    """