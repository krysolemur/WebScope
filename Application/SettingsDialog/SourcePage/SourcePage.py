# sourcepage.py

# Importing system files
import re 

from PySide6.QtWidgets import QSlider, QComboBox, QCheckBox, QPushButton, QDialog, QColorDialog, QWidget # type: ignore
from PySide6.QtCore import QSignalBlocker # type: ignore
from PySide6.QtGui import QColor # type: ignore

# Importing program files
from Application.QtFiles.StyleDialog import Ui_styleDialog
from Application.QtFiles.SourcePage import Ui_sourcePage

# Class with color picker
class SourcePage(QWidget):

    # Initiator
    def __init__(self, parent) -> None:
        '''
        Save parent, Ui, and other objects.
        '''

        # Init parent
        super().__init__(parent)

        # Get app
        self.app = parent.app

        '''
        Load Ui for page and setup page.
        '''

        # Load page
        self.ui = Ui_sourcePage()

        # Setup ui
        self.ui.setupUi(self)

        '''
        Variables.
        '''

        # Saved
        self.isSaved = True

        # Browse all buttons in button group
        for btn in self.stylingButtonGroup.buttons():
            # If it have not style attribut
            if not hasattr(btn, 'style'):
                # Add it
                btn.style = {
                    "color": "none", "background-color": "none", 
                    "font-weight": "none", "font-style": "none", 
                    "text-decoration": "none", "transform": "none"
                }
                
        # Připojení tlačítek kategorií
        self.ui.btn_sel_tags.clicked.connect(self._loadStyle)
        self.ui.btn_sel_attrs.clicked.connect(self._loadStyle)
        self.ui.btn_sel_strings.clicked.connect(self._loadStyle)
        self.ui.btn_sel_comments.clicked.connect(self._loadStyle)

        # Připojení nástrojů (B, I, Color atd.)
        self.ui.btn_style_color.clicked.connect(self._setForeground)
        # self.ui.btn_style_bg.clicked.connect(self._setBackground) # Pokud ho v UI máš
        self.ui.btn_style_bold.clicked.connect(self._setBold)
        self.ui.btn_style_italic.clicked.connect(self._setItalic)
        
        # Defaultní výběr první kategorie po startu
        self.ui.btn_sel_tags.setChecked(True)
        self._loadStyle()

        '''
        Connect actions and run setup functions.
        '''

        # Set tracking
        self._connectChangesTracking()

    '''
    Style methods.
    '''

    # Encode style
    def _encodeStyle(self) -> dict:
        # Returnt stylesheet
        return {
            "color": self.foregroundColor,
            "background-color": self.backgroundColor,
            "font-weight": self.boldStyle,
            "font-style": self.italicStyle,
            "text-decoration": self.underlineStyle,
            "transform": self.ui.transformStyle.currentText().lower()
        }

    # Decode style
    def _decodeStyle(self) -> None:
        self.foregroundColor = self.selected.style["color"]
        self.backgroundColor = self.selected.style["background-color"]
        self.boldStyle = self.selected.style["font-weight"]
        self.italicStyle = self.selected.style["font-style"]
        self.underlineStyle = self.selected.style["text-decoration"]
        self.transform = self.selected.style["transform"]

    # Reset style
    def _resetStyle(self) -> None:
        self.foregroundColor = "none"

        self.backgroundColor = "none"

        self.boldStyle = "none"

        self.italicStyle = "none"

        self.underlineStyle = "none"

        self.ui.underlineStyle.setChecked(False)
        self.ui.italicStyle.setChecked(False)
        self.ui.boldStyle.setChecked(False)

        self.ui.transformStyle.setCurrentIndex(0)

        self.selected.style = self._encodeStyle()

        self._loadStyle()

        self.isSaved = False

    # Load style
    def _loadStyle(self) -> None:
        # Set selected
        self.selected = self.ui.stylingButtonGroup.checkedButton()

        # Decode style
        self._decodeStyle()
        
        self.ui.foregroundStyle.setStyleSheet(f"""
            color: {self.foregroundColor};                    
        """)

        self.ui.backgroundStyle.setStyleSheet(f"""
            background-color: {self.backgroundColor};                    
        """)

        self.ui.boldStyle.setStyleSheet(f"""
            font-weight: {self.boldStyle};                    
        """)

        self.ui.italicStyle.setStyleSheet(f"""
            font-style: {self.italicStyle};                    
        """)

        self.ui.underlineStyle.setStyleSheet(f"""
            text-decoration: {self.underlineStyle};                    
        """)

        self.ui.underlineStyle.setChecked(self.underlineStyle == "underline")
        self.ui.italicStyle.setChecked(self.italicStyle == "italic")
        self.ui.boldStyle.setChecked(self.boldStyle == "bold")

    # Foreground
    def _setForeground(self) -> None:
        # Open color dialog
        color = QColorDialog.getColor()

        # Check if color is valid
        if color.isValid():
            # Get HEX color name
            hex_color = color.name()

            self.ui.foregroundStyle.setStyleSheet(f"""
                color: {hex_color};                    
            """)

            self.foregroundColor = hex_color

        self.selected.style = self._encodeStyle()

        self.isSaved = False
        
    # Background
    def _setBackground(self) -> None:
        # Open color dialog
        color = QColorDialog.getColor()

        # Check if color is valid
        if color.isValid():
            # Get HEX color name
            hex_color = color.name()

            self.ui.backgroundStyle.setStyleSheet(f"""
                background-color: {hex_color};                    
            """)

            self.backgroundColor = hex_color
        
        self.selected.style = self._encodeStyle()

        self.isSaved = False

    # Bold
    def _setBold(self) -> None:
        if self.ui.boldStyle.isChecked():
            self.ui.boldStyle.setStyleSheet(f"""
                font-weight: bold;                    
            """)
            self.boldStyle = "bold"
        else:
            self.ui.boldStyle.setStyleSheet(f"""
                font-weight: none;                    
            """)       
            self.boldStyle = "none"

        self.selected.style = self._encodeStyle()

        self.isSaved = False

    # Italic
    def _setItalic(self) -> None:
        # If checked
        if self.ui.italicStyle.isChecked():
            self.ui.italicStyle.setStyleSheet(f"""
                font-style: italic;                    
            """)
            self.italicStyle = "italic"
        else:
            self.ui.italicStyle.setStyleSheet(f"""
                font-style: none;                    
            """)
            self.italicStyle = "none"

        self.selected.style = self._encodeStyle()

        self.isSaved = False

    # Underline
    def _setUnderline(self) -> None:
        if self.ui.underlineStyle.isChecked():
            self.ui.underlineStyle.setStyleSheet(f"""
                text-decoration: underline;                    
            """)
            self.underlineStyle = "underline"
        else:
            self.ui.underlineStyle.setStyleSheet(f"""
                text-decoration: none;                    
            """)
            self.underlineStyle = "none"

        self.selected.style = self._encodeStyle()

        self.isSaved = False

    '''
    Settings methods.
    '''

    # Load settings function
    def loadSettings(self, settings) -> None:
        # Save settings
        self.settings = settings

        # Browse all keys and their values
        for key, value in settings.items():
            # Get widget by name
            widget = getattr(self.ui, key, None)

            # If widget is None, skip
            if widget is None:
                continue
            
            # Block signals
            widget.blockSignals(True)

            # Check instances
            if isinstance(widget, QCheckBox):
                # Set value for checkbox
                widget.setChecked(bool(value))
            elif isinstance(widget, QPushButton):
                # Check if button is checkable
                if widget.isCheckable():
                    # Load style
                    widget.style = self.settings.get(widget.objectName())      

            # Block signals
            widget.blockSignals(False)

        
        # Load style
        self._loadStyle()

    # Get settings from childs
    def getSettings(self) -> dict:
        # Tady sestavíme slovník přesně podle jmen v UI a v configu
        return {
            # Styly pro jednotlivé typy kódu
            "btn_sel_tags": self.ui.btn_sel_tags.style if hasattr(self.ui.btn_sel_tags, 'style') else {},
            "btn_sel_attrs": self.ui.btn_sel_attrs.style if hasattr(self.ui.btn_sel_attrs, 'style') else {},
            "btn_sel_strings": self.ui.btn_sel_strings.style if hasattr(self.ui.btn_sel_strings, 'style') else {},
            "btn_sel_comments": self.ui.btn_sel_comments.style if hasattr(self.ui.btn_sel_comments, 'style') else {},
            
            # Pokročilé nastavení editoru (hodnoty z checkboxů a spinboxů)
            "chk_auto_close": self.ui.chk_auto_close.isChecked(),
            "chk_line_numbers": self.ui.chk_line_numbers.isChecked(),
            "chk_word_wrap": self.ui.chk_word_wrap.isChecked(),
            "chk_format_save": self.ui.chk_format_save.isChecked(),
            
            # Pokud jsi přidal i výběr transformace textu
            "cb_style_transform": self.ui.cb_style_transform.currentText()
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
            # # Check if is checkabel
            # if button.isCheckable():
            #     # Connect the toggle signal to the dirty state tracker for checkable buttons.
            #     button.clicked.connect(self._markAsDirty)
            None

    # Function that change isSaved status if somethings is saved.
    def _markAsDirty(self) -> None:
        # Change saved status
        self.isSaved = False
