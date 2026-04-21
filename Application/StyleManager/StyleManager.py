# stylesheet.py

# Import system modules

# Import program files
from Application.StyleManager.StyleCreator import StyleCreator

# Class stylesheet
class StyleManager:

    # Stylesheet dir
    styleDir = "resources/Stylesheets"
    
    # Initiator
    def __init__(self) -> None:

        # None
        None
    
    # Create sheet
    def create_sheet(self) -> None:
        # Create instance
        styleCreator = StyleCreator()

        # Exec
        styleCreator.exec()