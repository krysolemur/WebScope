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
        Init parents and set important variables.
        '''

        # Init parents
        super().__init__()

        # Defautl themes
        self.defaultThemes = {
            "Dark": lambda: self.loadPalette("Dark"),
            "Light": lambda: self.loadPalette("Light")
        }

        # Themes directory path
        self.themeDir = "resources/Themes"


        # All themes
        self.themes = self._getThemes

        # Get themes
        self.themes()

    '''
    Private functions.
    '''

    # Browse button function thats open browse dialog and after open file button, set path to line edit.
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

        # Set whole absolute path to QLineEdit
        self.ui.addLineEdit.setText(filename)

    # Get all themes function, return list of all .json files that can be used for storing palette.
    def _getThemes(self) -> list:
        # Create new list
        themes = []

        # List through themes direcotyr
        for theme in os.listdir(self.themeDir):
            # Check if its not directory
            if not os.path.isdir(f"{self.themeDir}/{theme}"):
                # Check python type
                if theme.endswith(".json"):
                    # Append it to the theme list
                    themes.append(str(theme))

        # Return themes
        return themes

    # Add theme function with fast validation if theme path exists or if its even entered.
    def _addTheme(self, path) -> None:
        # Set statusLabel stylesheet
        self.ui.statusLabel.setStyleSheet("color: #ff0000")

        # Check path if its even entered
        if not path:
            # Set error text
            self.ui.statusLabel.setText("Enter path!")

            return

        # Check if path exists
        if not os.path.exists(path):
            # Set error text
            self.ui.statusLabel.setText("Path does not exists!")

            return 

        # Accept close
        self.close()

    '''
    Public functions.
    '''

    # Add theme dialog for adding themes, browsing files and copying it to application theme folder.
    def getTheme(self) -> None:
        '''
        Create dialog, load ui and setup it.
        '''

        # Create themeDialog
        themeDialog = QDialog()

        print("Fd")

        # Load ui
        themeDialogUi = Ui_ThemeDialog()

        # Setup ui
        themeDialogUi.setupUi(themeDialog)

        '''
        Setup window like title, size and more.
        '''

        # Set title for theme dialog
        themeDialog.setWindowTitle("Add theme")

        # Set minimum size counted by qt
        themeDialog.setMinimumSize(themeDialog.sizeHint())

        # Resize to default size hint
        themeDialog.resize(themeDialog.sizeHint())

        '''
        Button actions.
        '''

        # Connect browse button action
        themeDialogUi.browseButton.clicked.connect(self._browseThemes)

        # Add theme button action
        themeDialogUi.addButton.clicked.connect(lambda: self._addTheme(themeDialogUi.addLineEdit.text()))

        # Run dialog
        themeDialog.exec()

    # Parse JSON palette to python and apply it if its ok by keys.
    def parsePalette(self, palette):
        # Check if file exists
        if not os.path.exists(f"{self.theme_dir}/{palette}") or not palette.endswith(".json"):
            # Show error
            self.printe(msg=f"Wrong palette {palette}", exception=None, function=self.parseJSONPalette.__name__)

            # Return error
            return False
        
        # Load data from palette
        with open(f"{self.theme_dir}/{palette}", "r") as theme:
            # Load data
            data = json.load(theme)
            
        # Create new empty palette
        palette = QPalette()

        # Try set colors for new palette
        try:
            # Texts
            palette.setColor(QPalette.WindowText, data["QPalette.WindowText"])
            palette.setColor(QPalette.Text, data["QPalette.Text"])
            palette.setColor(QPalette.ButtonText, data["QPalette.ButtonText"])
            palette.setColor(QPalette.BrightText, data["QPalette.BrightText"])
            palette.setColor(QPalette.PlaceholderText, data["QPalette.PlaceholderText"])

            # Backgrounds
            palette.setColor(QPalette.Window, data["QPalette.Window"])
            palette.setColor(QPalette.Base, data["QPalette.Base"])
            palette.setColor(QPalette.AlternateBase, data["QPalette.AlternateBase"])
            palette.setColor(QPalette.Button, data["QPalette.Button"])
            palette.setColor(QPalette.ToolTipBase, data["QPalette.ToolTipBase"])
            palette.setColor(QPalette.ToolTipText, data["QPalette.ToolTipText"])

            # 3D and shadows
            palette.setColor(QPalette.Shadow, data["QPalette.Shadow"])
            palette.setColor(QPalette.Light, data["QPalette.Light"])
            palette.setColor(QPalette.Midlight, data["QPalette.Midlight"])
            palette.setColor(QPalette.Mid, data["QPalette.Mid"])
            palette.setColor(QPalette.Dark, data["QPalette.Dark"])

            # Selecting interactive
            palette.setColor(QPalette.Highlight, data["QPalette.Highlight"])
            palette.setColor(QPalette.HighlightedText, data["QPalette.HighlightedText"])
            palette.setColor(QPalette.Link, data["QPalette.Link"])
            palette.setColor(QPalette.LinkVisited, data["QPalette.LinkVisited"])

            # Disabled...
            palette.setColor(QPalette.Disabled, QPalette.WindowText, data["Disabled.WindowText"])
            palette.setColor(QPalette.Disabled, QPalette.Text, data["Disabled.Text"])
            palette.setColor(QPalette.Disabled, QPalette.ButtonText, data["Disabled.ButtonText"])
            palette.setColor(QPalette.Disabled, QPalette.Base, data["Disabled.Base"])

            # Return palette
            return palette
        except KeyError as e:
            # Show error
            self.printe(msg=f"Error while loading palette {palette}", exception=e, function=self.parseJSONPalette.__name__)

            # Return error
            return False

    # Function that load build in Dark or Light palette.
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