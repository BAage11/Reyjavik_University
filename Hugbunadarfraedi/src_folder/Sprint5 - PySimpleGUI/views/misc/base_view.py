from abc import ABCMeta, abstractmethod
from views.misc.component_interface import ComponentInterface

""" 
GuiWindow is the base class that other windows inherit from, 
it contains the user object and the connection object. This
allows other classes to access those variables.
"""
class GuiWindow(metaclass=ABCMeta):

    def __init__(self, user):

        self.user = user
        self.actions = ComponentInterface()
        self.connection = ""
        super().__init__()
    
    """
    show_window() displays the window when it is called, it is marked
    abstract since it needs to be implemented in other classes since each
    window is different, and also for consistency.
    """
    @abstractmethod
    def show_window(self):
        pass
    
    """
    switch_windows() closes the current window and opens up the next one for
    the user to see.
    """
    def switch_windows(self, current_window, new_window):
        current_window.Close()
        new_window.show_window()
    
    """
    hard_exit() simply terminates the python program effectively
    """
    def hard_exit(self):
        exit()