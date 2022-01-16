from views.misc.services.connection import Connection

class RentalService(Connection):

    """
    Returns a dictionary of all rentals in the system
    """
    def get_all_rentals(self):
        model = {"op": "get_all_rentals"}
        return self.execute(model)

    
    def create_rental(self, lender_id, book_id, renter_id):
        model = {"op": "create_rental",
                 "rental_model": {
                     "lender_id": lender_id,
                     "book_id": book_id,
                     "renter_id": renter_id
                 }}
        return self.execute(model)