# sourcepage.py

# Importing system files
import re 

from PySide6.QtWidgets import QSlider, QComboBox, QCheckBox, QPushButton, QDialog, QColorDialog, QWidget # type: ignore
from PySide6.QtCore import QSignalBlocker # type: ignore

# Importing program files
from libs.QtGuiFiles.PyFiles.StyleDialog import Ui_styleDialog
from libs.QtGuiFiles.PyFiles.SourcePage import Ui_sourcePage

# Class with color picker
class SourcePage(QWidget):
    def __init__(self, parent) -> None:
        '''
        Save parent, Ui, and other objects.
        '''

        # Init parent
        super().__init__(parent)

        # Save parent
        self.parent = parent

        '''
        Load Ui for page and setup page.
        '''

        # Load page
        self.ui = Ui_sourcePage()

        # Setup ui
        self.ui.setupUi(self)

        # Set minimum size
        self.setMinimumSize(self.sizeHint())

        '''
        Variables.
        '''

        # Saved
        self.isSaved = True

        '''
        Connect actions and run setup functions.
        '''

        # Set tracking
        self._connectChangesTracking()

        # Html elements style button action
        self.ui.htmlElementsButton.clicked.connect(lambda: self._stylePicker(self.ui.htmlElementsButton))

        # Html elements style button action
        self.ui.htmlAtributsButton.clicked.connect(lambda: self._stylePicker(self.ui.htmlAtributsButton))

        # Html elements style button action
        self.ui.atributsValuesButton.clicked.connect(lambda: self._stylePicker(self.ui.atributsValuesButton))

    # Logic for a custom style picker dialog designed for HTML text elements.
    def _stylePicker(self, button) -> str:
        '''
        Default exmaple text values.
        '''

        # Foreground
        self.fg = "black"

        # Background
        self.bg = "transparent"

        # Weight
        self.weight = "normal"

        # Style
        self.style = "normal"

        # Underline
        self.under = "none"

        # Transform
        self.transform = "none"

        '''
        Dialog initialization, UI loading, and widget setup.
        '''

        # Create a new QDialog instance with the main window as its parent.
        self.styleDialog = QDialog(self)

        # Instantiate the generated UI layout for the style picker.
        self.styleDialogUi = Ui_styleDialog()

        # Apply the layout and widgets to the newly created dialog instance.
        self.styleDialogUi.setupUi(self.styleDialog)

        '''
        Configuring dialog window properties like geometry and titles.
        '''

        # Prevent the user from shrinking the window below its calculated size hint.
        self.styleDialog.setMinimumSize(self.styleDialog.sizeHint())

        # Set the initial dimensions of the dialog based on its layout needs.
        self.styleDialog.resize(self.styleDialog.sizeHint())

        # Define the title displayed in the window's title bar.
        self.styleDialog.setWindowTitle(f"{self.app.name} | {self.app.version} | Style picker")

        '''
        Establishing signal and slot connections for interactive widgets.
        '''

        # Trigger color selection for the text foreground on button click.
        self.styleDialogUi.foregroundButton.clicked.connect(lambda: self._getColor(self.styleDialogUi.foregroundButton))

        # Trigger color selection for the text background on button click.
        self.styleDialogUi.backgroundButton.clicked.connect(lambda: self._getColor(self.styleDialogUi.backgroundButton))     

        # Update the live preview whenever the bold toggle is clicked.
        self.styleDialogUi.boldButton.clicked.connect(self._updatePreview)        

        # Update the live preview whenever the italic toggle is clicked.
        self.styleDialogUi.italicButton.clicked.connect(self._updatePreview)      

        # Update the live preview whenever the underline toggle is clicked.
        self.styleDialogUi.underlineButton.clicked.connect(self._updatePreview)      

        # Update the live preview whenever the text case selection changes.
        self.styleDialogUi.caseComboBox.currentIndexChanged.connect(self._updatePreview)

        # Execute the encoding logic when the user confirms with the OK button.
        self.styleDialogUi.okButton.clicked.connect(lambda: (button.setStyleSheet(self.styleDialogUi.exampleTextLabel.styleSheet()), self.styleDialog.accept()))

        # Trigger the style reset logic whenever the reset button is clicked.
        self.styleDialogUi.resetButton.clicked.connect(self._resetStyles)
        
        # Display the dialog as a modal window and capture the return result.
        result = self.styleDialog.exec()

        # Evaluate if the dialog was closed via the OK button (Accepted).
        if result == QDialog.Accepted:
            # Return the CSS string captured during the encoding process.
            return getattr(self, 'css', "")
        
        # Return an empty string if the user cancelled or closed the dialog.
        return ""

    # Nested function to clear all custom style selections and refresh the UI.
    def _resetStyles(self) -> None:
        # Revert color variables to their default states.
        self.fg = "black"

        # Background
        self.bg = "transparent"

        # Weight
        self.weight = "normal"

        # Style
        self.style = "normal"

        # Underline
        self.under = "none"

        # Transform
        self.transform = "none"

        # Uncheck all styling toggle buttons.
        self.styleDialogUi.boldButton.setChecked(False)
        self.styleDialogUi.italicButton.setChecked(False)
        self.styleDialogUi.underlineButton.setChecked(False)

        # Reset the text case selection to the first index (None).
        self.styleDialogUi.caseComboBox.setCurrentIndex(0)

        # Update preview
        self._updatePreview()

    # Update example label preview
    def _updatePreview(self) -> None:
        # Determine the font weight CSS property based on the bold toggle button state.
        self.weight = "bold" if self.styleDialogUi.boldButton.isChecked() else "normal"

        # Determine the font style CSS property based on the italic toggle button state.
        self.style = "italic" if self.styleDialogUi.italicButton.isChecked() else "normal"

        # Determine the text decoration CSS property based on the underline toggle button state.
        self.under = "underline" if self.styleDialogUi.underlineButton.isChecked() else "none"

        # Retrieve the current selection index from the text case combo box.
        index = self.styleDialogUi.caseComboBox.currentIndex()

        # Define a mapping dictionary to translate UI indices into CSS text-transform values.
        mapping = {1: "uppercase", 2: "lowercase"}

        # Assign the corresponding transformation string or default to "lowercase" if the index is missing.
        self.transform = mapping.get(index, "lowercase")

        # Apply the generated CSS-like stylesheet to the preview label.
        self.styleDialogUi.exampleTextLabel.setStyleSheet(f"""
            color: {self.fg};
            background-color: {self.bg};
            font-weight: {self.weight};
            font-style: {self.style};
            text-decoration: {self.under};
            text-transform: {self.transform};
        """)

        # Evaluate if any styling attribute differs from its default state.
        has_changes = (
            self.fg != 'black' or self.bg != 'transparent' or 
            self.styleDialogUi.boldButton.isChecked() or 
            self.styleDialogUi.italicButton.isChecked() or 
            self.styleDialogUi.underlineButton.isChecked() or
            self.styleDialogUi.caseComboBox.currentIndex() != 0
        )
        
        # Toggle the reset button's availability based on the presence of changes.
        self.styleDialogUi.resetButton.setEnabled(has_changes)

    # Get color
    def _getColor(self, button) -> None:
        # Invoke the standard Qt color dialog to let the user pick a color.
        color = QColorDialog.getColor()

        # Verify that the user confirmed the selection and didn't cancel.
        if color.isValid():
            # Determine if the foreground button triggered the change.
            if button == self.styleDialogUi.foregroundButton:
                # Store the selected hex color as the current foreground.
                self.fg = color.name()
            # Determine if the background button triggered the change.
            elif button == self.styleDialogUi.backgroundButton:
                # Store the selected hex color as the current background.
                self.bg = color.name()
            
            # Refresh the preview label to reflect the new color selection.
            self._updatePreview()

    # Encodes the style by scraping values directly from the button's current stylesheet.
    def encodeStyle(self, button) -> list:
        # Retrieve the raw CSS string from the button widget.
        stylesheet = button.styleSheet()

        # Use regex to find all values situated between a colon and a semicolon.
        # Example: "color: #ffffff;" -> ["#ffffff"]
        style_list = re.findall(r":\s*([^;]+)", stylesheet)

        # Note: If 'text-transform' was stripped by Qt, this list will be shorter than expected (missing index 5).

        # Close the style dialog and confirm the selection.
        self.styleDialog.accept()

        # Return the extracted values as a list.
        return style_list

    # Converts a style configuration list into a formatted CSS stylesheet string.
    def decodeStyle(self, style) -> str:
        # Extract foreground and background colors from the first two elements.
        fg = style[0]
        bg = style[1]

        # Extract styling flags (Note: these are likely Booleans and need conversion for CSS).
        weight = style[2]
        styles = style[3]
        under = style[4]

        # Extract the text transformation setting (e.g., uppercase, lowercase, none).
        transform = style[5]

        '''
        Construct the final stylesheet string using the extracted variables.
        Warning: Qt's setStyleSheet does not natively support 'text-transform'.
        '''
        
        stylesheet = f"""
            color: {fg};
            background-color: {bg};
            font-weight: {weight};
            font-style: {styles};
            text-decoration: {under};
            text-transform: {transform};
        """

        # Return the multi-line string to be applied to a widget.
        return stylesheet

    '''
    Settings methods.
    '''

    # Load settings function
    def loadSettings(self, settings) -> None:
        # Browse all keys and their values
        for key, value in settings.items():
            # Get widget by name
            widget = getattr(self.ui, key, None)

            # If widget is None, skip
            if widget is None:
                continue

            widget.blockSignals(True)

            # Check instances
            if isinstance(widget, QCheckBox):
                # Set value for checkbox
                widget.setChecked(bool(value))

            widget.blockSignals(False)

    # Get settings from childs
    def getSettings(self) -> dict:
        # Return settings
        return {
            "htmlElementsCheckBox": self.ui.htmlElementsCheckBox.isChecked(),
            "htmlAtributsCheckBox": self.ui.htmlAtributsCheckBox.isChecked(),
            "atributsValuesCheckBox": self.ui.atributsValuesCheckBox.isChecked()
        }

    '''
    Marking as not saved.
    '''

    # Automatically discovers input widgets and connects their change signals to the dirty state tracker.
    def _connectChangesTracking(self) -> None:
        container = self.ui.sourceCodeScrollContent
        # Locate all combo box widgets within the current window and its children.
        for combo in container.findChildren(QComboBox):
            # Trigger the dirty flag whenever a different item is selected in a combo box.
            combo.currentIndexChanged.connect(self._markAsDirty)
            
        # Locate all slider widgets within the UI.
        for slider in container.findChildren(QSlider):
            # Trigger the dirty flag whenever the slider handle is moved to a new value.
            slider.valueChanged.connect(self._markAsDirty)
            
        # Locate all checkbox widgets within the UI.
        for checkbox in container.findChildren(QCheckBox):
            # Trigger the dirty flag whenever a checkbox is toggled on or off.
            checkbox.stateChanged.connect(self._markAsDirty)

        # Locate all push button widgets within the UI.
        for button in container.findChildren(QPushButton):
            # Check if is checkabel
            if button.isCheckable():
                # Connect the toggle signal to the dirty state tracker for checkable buttons.
                button.clicked.connect(self._markAsDirty)

    # Function that change isSaved status if somethings is saved.
    def _markAsDirty(self) -> None:
        # Change saved status
        self.isSaved = False