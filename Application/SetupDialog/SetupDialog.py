# SetupDialog.py

from PySide6.QtWidgets import QDialog # type: ignore

from Application.QtFiles.SetupDialog import Ui_setupDialog

# Modal dialog responsible for application pre-configuration and environment checks
class SetupDialog(QDialog):

    # Initiator
    def __init__(self):
        # Proccess variables
        self.proccess = [

        ]

        # Init parents
        super().__init__()

        # Create UI instance
        self.ui = Ui_setupDialog()

        # Build UI components
        self.ui.setupUi(self)

        # Format window title
        #self.setWindowTitle(f"{Application.name} | {Application.version} | Initializing")

        # Set minimum size hint
        self.setMinimumSize(self.sizeHint())

        # Resize to fixed dimensions
        self.resize(600, 75)

        # Execute modal dialog
        # TODO: Relocate .exec() call to the factory/caller to prevent blocking during instantiation
        self.exec()

    # Validate the availability of external network resources
    def check_network_connection(self):

        """Update the interface to reflect the current network diagnostic state."""

        # Update status label
        self.ui.loading_label.setText("Checking for internet connection")

    # Verify the local application version against the remote repository
    def check_for_updates(self):

        """Evaluate user preferences to determine if update checks should proceed."""

        # Check configuration value
        if self.config["GeneralPage"]["check_updates_combo_box"] == "Yes":

            """Update UI and initiate the remote fetching logic."""

            # Update status label
            self.ui.loading_label.setText("Checking for updates")

        # Exit if disabled
        else:

            # Interrupt function execution
            return

        """Verify the integrity of the local configuration storage."""

        # Update status label
        # TODO: Implement actual directory validation logic here
        self.ui.loading_label.setText("Checking config directory")