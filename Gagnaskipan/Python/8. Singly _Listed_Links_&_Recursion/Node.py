class Node():

    def __init__(self, data = None, next_ = None):
        self.data = data
        self.next = next_

    def get_next(self):
        return self.next