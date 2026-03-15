# window.py

# Importing Qt
from PySide6.QtWidgets import QMainWindow # type: ignore

# Main class window for managing window and loading GUI
class Window(QMainWindow):
    def __init__(self, app):
        # Init QMainWindow
        super().__init__()

        # Save parent 
        self.app = app

        '''
        Windows properties like size, title, and more
        '''

        # Title
        self.setWindowTitle(f"WebScope | {self.app.version}")  

        # Size
        self.resize(800, 600) 



