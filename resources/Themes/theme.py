# theme.py

# Import system modules
import json
import os

from PySide6.QtWidgets import QDialog, QFileDialog # type: ignore
from PySide6.QtGui import QPalette, QColor # type: ignore
from PySide6.QtCore import Qt # type: ignore

# Import profram files
from libs.Logging.logging import Logging

from libs.QtGuiFiles.PyFiles.ThemeDialog import Ui_ThemeDialog

# Class Theme
class Theme(Logging):
    def __init__(self) -> None:
        '''
        Init parents and set imoprtant variables.
        '''

        # Init parents
        super().__init__()

        # Theme directory
        self.theme_dir = "resources/Themes"

        # Defautl themes
        self.default_themes = {
            "Default": None,
            "Dark": None,
            "Light": None
        }

        # All themes
        self.themes = self._getThemes

        # Get themes
        self.themes()

    '''
    Private functions.
    '''

    # Browse button function
    def _browseThemes(self) -> None:
        # Get filename from QFileDialog
        filename, _ = QFileDialog.getOpenFileName(
            self,
            # Title
            "Choose file",
            # Default folder
            "",  
            # Accept types
            "Python files (*.py);;"
        )

        # Set to QLineEdit
        self.ui.addLineEdit.setText(filename)

    # Get all themes
    def _getThemes(self) -> list:
        # Create new list
        themes = []

        # List through themes direcotyr
        for theme in os.listdir(self.theme_dir):
            # Check if its not directory
            if not os.path.isdir(f"{self.theme_dir}/{theme}"):
                # Check python type
                if theme.endswith(".py"):
                    # Append it to the theme list
                    themes.append(str(theme))

        # Return themes
        return themes

    # Add theme
    def _addTheme(self, path) -> None:
        # Set statusLabel stylesheet
        self.ui.statusLabel.setStyleSheet("color: #ff0000")

        # Check path
        if not path:
            # Set error text
            self.ui.statusLabel.setText("Enter path!")

            return

        # Check if path exists
        if not os.path.exists(path):
            # Set error text
            self.ui.statusLabel.setText("Path does not exists!")

            return 

        # Accept
        self.close()

    '''
    Public functions.
    '''

    # Add theme dialog
    def themeDialog(self) -> None:
        '''
        Create dialog, load ui and setup it.
        '''

        ThemeDialog = QDialog()

        # Load ui
        ThemeDialogUi = Ui_ThemeDialog()

        # Setup ui
        ThemeDialogUi.setupUi(ThemeDialog = QDialog())

        '''
        Setup window like title, size and more.
        '''

        # Title
        ThemeDialog.setWindowTitle("Add theme")

        # Minimum size
        ThemeDialog.setMinimumSize(ThemeDialog.sizeHint())

        # Resize
        ThemeDialog.resize(ThemeDialog.sizeHint())

        '''
        Button actions.
        '''

        # Browse button action
        ThemeDialog.ui.browseButton.clicked.connect(self._browseThemes)

        # Add theme button action
        ThemeDialog.ui.addButton.clicked.connect(lambda: self._addTheme(ThemeDialogUi.addLineEdit.text()))

    # Parse JSON palette
    def parseJSONPalette(self) -> None:
        None

    '''
    Load palette function.
    '''

    # Load light or dark palette
    def loadPalette(self, palette):
        # Check if palette is dark
        if palette == "Dark":
            # Create new palette 
            dark_palette = QPalette()

            # Define colors
            background_color = QColor(45, 45, 45)
            alternate_background = QColor(35, 35, 35)
            text_color = QColor(225, 225, 225)
            disabled_color = QColor(127, 127, 127)
            highlight_color = QColor(42, 130, 218) # Pěkná modrá

            # Active window
            dark_palette.setColor(QPalette.Window, background_color)
            dark_palette.setColor(QPalette.WindowText, text_color)
            dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
            dark_palette.setColor(QPalette.AlternateBase, alternate_background)
            dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
            dark_palette.setColor(QPalette.ToolTipText, Qt.white)
            dark_palette.setColor(QPalette.Text, text_color)
            dark_palette.setColor(QPalette.Button, background_color)
            dark_palette.setColor(QPalette.ButtonText, text_color)
            dark_palette.setColor(QPalette.BrightText, Qt.red)
            dark_palette.setColor(QPalette.Link, highlight_color)
            dark_palette.setColor(QPalette.Highlight, highlight_color)
            dark_palette.setColor(QPalette.HighlightedText, Qt.black)

            # Disabled widgets
            dark_palette.setColor(QPalette.Disabled, QPalette.WindowText, disabled_color)
            dark_palette.setColor(QPalette.Disabled, QPalette.Text, disabled_color)
            dark_palette.setColor(QPalette.Disabled, QPalette.ButtonText, disabled_color)
            dark_palette.setColor(QPalette.Disabled, QPalette.Base, background_color)

            # Return dark palette
            return dark_palette
        elif palette == "Light":
            # Create new palette 
            light_palette = QPalette()

            # Define colors
            background_color = QColor(240, 240, 240)
            alternate_background = QColor(225, 225, 225)
            base_color = QColor(255, 255, 255)
            text_color = QColor(0, 0, 0)
            disabled_color = QColor(160, 160, 160)
            highlight_color = QColor(0, 120, 215) # Standardní Windows modrá

            # Active window
            light_palette.setColor(QPalette.Window, background_color)
            light_palette.setColor(QPalette.WindowText, text_color)
            light_palette.setColor(QPalette.Base, base_color)
            light_palette.setColor(QPalette.AlternateBase, alternate_background)
            light_palette.setColor(QPalette.ToolTipBase, Qt.white)
            light_palette.setColor(QPalette.ToolTipText, text_color)
            light_palette.setColor(QPalette.Text, text_color)
            light_palette.setColor(QPalette.Button, background_color)
            light_palette.setColor(QPalette.ButtonText, text_color)
            light_palette.setColor(QPalette.BrightText, Qt.red)
            light_palette.setColor(QPalette.Link, highlight_color)
            light_palette.setColor(QPalette.Highlight, highlight_color)
            light_palette.setColor(QPalette.HighlightedText, Qt.white)

            # Disabled widgets
            light_palette.setColor(QPalette.Disabled, QPalette.WindowText, disabled_color)
            light_palette.setColor(QPalette.Disabled, QPalette.Text, disabled_color)
            light_palette.setColor(QPalette.Disabled, QPalette.ButtonText, disabled_color)
            light_palette.setColor(QPalette.Disabled, QPalette.Base, background_color)

            # Return ligth palette
            return light_palette
        else: None