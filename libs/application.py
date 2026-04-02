# application.py

# Import system files
import os
import sys

from PySide6.QtWidgets import QApplication, QDialog # type: ignore
from PySide6.QtCore import QTimer # type: ignore
from PySide6.QtGui import QFont # type: ignore

# Importing program files
from libs.MainWindow.mainwindow import MainWindow
from Config.configmanager import ConfigManager
from libs.Logging.logging import Logging
from resources.Themes.theme import Theme

from libs.QtGuiFiles.PyFiles.SetupDialog import Ui_setupDialog
from libs.QtGuiFiles.PyFiles.CustomDialog import Ui_customDialog

# Class for managing whole application
class Application(Logging, QApplication):
    def __init__(self) -> None:
        '''
        Set all variables for application.
        '''

        # Version of application
        self.version = "0.1.0"

        # Application name
        self.name = "XyraEngine"

        # Icon path for application
        self.iconPath = ""

        # Starting info message
        self.printi(msg="Starting WebScope")

        '''
        Init all modules, parents.
        '''

        # Init Logging and QApplication with sys.argv for application
        super().__init__(sys.argv)

        # Init ConfigManager module
        self.config = ConfigManager()

        # Init Theme module
        self.theme = Theme()

        # Init MainWindow module
        self.window = MainWindow(self)

        ''' 
        Load general settings.
        '''

        # Set font and font size for whole application
        self.setFont(QFont(str(self.config.configuration["fontComboBox"]), int(self.config.configuration["fontSizeSlider"])))

        # Load theme for application
        self._loadPalette(self.config.configuration["themeComboBox"])

        '''
        Load UI for setupDialog.
        '''
        
        # Create dialog
        self.setupDialog = QDialog()

        # Load Ui file
        self.ui = Ui_setupDialog()

        # Setup Ui for setupDialog
        self.ui.setupUi(self.setupDialog)

        '''
        Set dialog properties, title, size and more.
        '''

        # Dilaog title
        self.setupDialog.setWindowTitle(f"{self.name} | {self.version} | Inicializing")

        # Dialog minimum size
        self.setupDialog.setMinimumSize(self.setupDialog.sizeHint())

        # Dialog default size
        self.setupDialog.resize(600, 75)

        # Show dialog
        self.setupDialog.show()

        '''
        Start running loop for running all setup functions.
        '''
        
        # Process index for couting all process
        self.processIndex = 0

        # Run all setup processes 
        self._runNextProcess()

    '''
    Private functions.
    '''

    # Run next proccess function which is calling all setup processes and logging it in setupdialog
    def _runNextProcess(self) -> None:
        # List of all proccesses with their labels
        allProcess = [
            self._checkNetworkConnection,
            *( [self._checkForUpdates] if self.config.configuration["checkUpdatesComboBox"] == "Yes" else [] )
        ]

        '''
        Run all proccess with try except block for catching errors.
        '''

        # Check if all process were runned
        if self.processIndex >= len(allProcess):
            # Close setup dialog
            self.setupDialog.close()

            # Show and run main window
            self.window.show()

            return  

        # Try-except for catching errors
        try:    
            # Get proccess 
            process = allProcess[self.processIndex]

            # Check if process is callable
            if process:
                # Run process
                process()

                # Print OK if process runed without problems
                self.printo(msg="", function=process.__name__)

                # Set green color for success to status label
                self.ui.statusLabel.setStyleSheet("color: #00ff00")

                # Set OK text to status label 
                self.ui.statusLabel.setText("OK")

                # Set progressBar value plus 100 devided by all proccess
                self.ui.loadingBar.setValue(self.ui.loadingBar.value() + (100 // len(allProcess)))
        except Exception as e:
            '''
            Set error look.
            '''

            # Print error message, more information
            self.printe(exception=e, msg="", function=self._runNextProcess.__name__)

            # Set red color text for errror
            self.ui.statusLabel.setStyleSheet("color: #ff0000")

            # Set error text to status label to tell user that something is wrong
            self.ui.statusLabel.setText("ERROR")

        # Next index for running next function
        self.processIndex += 1

        # Next function after 500ms countdown
        QTimer.singleShot(500, self._runNextProcess
)

    # Checking internet connection is necessary for application running and inspecting webs.
    def _checkNetworkConnection(self) -> None:
        # Set label text
        self.ui.loadingLabel.setText("Checking for internet connection")

    # Function that check for updates from github and show it with download button.
    def _checkForUpdates(self) -> None:
        # If checking updates are available
        if self.config.configuration["checkUpdatesComboBox"] == "Yes":
            # Set label text and search for updates
            self.ui.loadingLabel.setText("Checking for updates")
        else:
            return

        # Set label text
        self.ui.loadingLabel.setText("Checking config directory")

    # Method that load function from theme.py or own theme, must be parsed by parseJSONPalette function in theme.py.
    def _loadPalette(self, palette) -> None:
        # Check if palette is default
        if palette == "Default":
            # Do not load any palette for default
            return
        
        # Check if palette is build in theme
        if palette in self.theme.defaultThemes.keys():
            # Load build in palette using directory that stored function with palette argument
            self.setPalette(self.theme.defaultThemes[palette]())

            return

        # Parse another palette from system
        if self.theme.parsePalette(palette):
            # Load palete if its parsed
            self.setPalette(self.theme.loadPalette(palette))
        else:
            # Log warn
            self.printw(msg="Loading default palette")

            # Do not load any palette for default

    '''
    Public functions.
    '''

    # Restart function for restarting application. Saved sys arguments, closed application and runned it again. Used in mainwindow.py.
    def restartApplication(self) -> None:
        '''
        Load ui for custom restart dialog.
        '''

        # Create dialog
        restartDialog = QDialog(self.window)

        # Load Ui
        restartDialogUi = Ui_customDialog()

        # Setup Ui 
        restartDialogUi.setupUi(restartDialog)

        '''
        Set properties for custom dialog like title, size and center it.
        '''

        # Dialog title
        restartDialog.setWindowTitle(f"{self.name} | {self.version} | Restart")

        # Adjust dialog size
        restartDialog.adjustSize()

        '''
        Set parametres for buttons and others childs.
        '''

        # Set label text
        restartDialogUi.textLabel.setText("Do you really want to restart application?")

        # Change cancel button text
        restartDialogUi.cancelButton.setText("No")

        # Change sumbit button text
        restartDialogUi.sumbitButton.setText("Yes")

        # Set cancel button action to close dialog
        restartDialogUi.cancelButton.clicked.connect(restartDialog.close)

        # Set sumbit button action for restart dialog with same parametres as before
        restartDialogUi.sumbitButton.clicked.connect(lambda: (self.printi(msg="Restarting application"), os.execv(sys.executable, [sys.executable] + sys.argv)))

        # Exec dialog, can not continue with open restart dialog
        restartDialog.exec()