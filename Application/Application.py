# Application.py

# Import system files
import os
import sys
import logging

from logging.handlers import RotatingFileHandler

from PySide6.QtWidgets import QApplication, QDialog # type: ignore
from PySide6.QtGui import QFont # type: ignore

# Importing program files
from Application.MainWindow.MainWindow import MainWindow

from Application.QtFiles.CustomDialog import Ui_customDialog

from Application.SetupDialog.SetupDialog import SetupDialog

from Config.configmanager import ConfigManager

from resources.Themes.ThemesManager import ThemesManager

# Class for managing whole application
class Application(QApplication):

    '''
    Usefull variables without inicializing.
    '''

    # Version 
    version = "0.1.0"

    # Application name
    name = "XyraEngine"
    
    # Icon path
    iconPath = ""

    # Initiator
    def __init__(self, args) -> None:

        # Init parents
        super().__init__(args)

        # Setup dialog object
        self.SetupDialog = SetupDialog()

        # Config object
        self.ConfigManager = ConfigManager()

        # Init theme manager
        self.ThemesManager = ThemesManager()

        # Setup application
        self._setupApplication()

        
    '''
    Private functions.
    '''

    # Setup function that loads general settings
    def _setupApplication(self) -> None:
        # Get configuration
        self.config = self.ConfigManager.loadSettings()

        # Font size dictonary
        fontSize = {
            "Large": 12,
            "Medium (recommended)": 10,
            "Small": 8
        }

        # Set font and font size for whole application
        self.setFont(QFont(str(self.config["GeneralPage"]["fontComboBox"]), int(fontSize[str(self.config["GeneralPage"]["fontSizeComboBox"])])))

        # Load theme for application
        self._loadTheme(self.config["GeneralPage"]["themeComboBox"])

        # Load stylesheet for application
        self._loadStylesheet(None)

    # Start main window
    def _startMainWindow(self) -> None:
        # Init MainWindow module
        self.MainWindow = MainWindow(self)

        # Show and run main window
        self.MainWindow.show()

    # Method that load function from theme.py or own theme, must be parsed by parseJSONPalette function in theme.py.
    def _loadTheme(self, palette) -> None:
        # Check if palette is default
        if palette == "Default":
            # Do not load any palette for default
            return
        
        # Check if palette is build in theme
        if palette in self.ThemesManager.defaultThemes.keys():
            # Load build in palette using directory that stored function with palette argument
            self.setPalette(self.ThemesManager.defaultThemes[palette]())

            return

        # Parse another palette from system
        if self.ThemesManager.parsePalette(palette):
            # Load palete if its parsed
            self.setPalette(self.ThemesManager.loadPalette(palette))
        else:
            None

            # Do not load any palette for default

    # Load stylesheet
    def _loadStylesheet(self, stylesheet) -> None:
        None

    '''
    Public functions.
    '''

    # Restart function for restarting application. Saved sys arguments, closed application and runned it again. Used in mainwindow.py.
    def restartApplication(self) -> None:
        # Restart command
        os.execv(sys.executable, [sys.executable] + sys.argv)
