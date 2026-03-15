# main.py

# Importing system files
import sys
import signal
import os
import traceback

from PySide6.QtWidgets import QApplication # type: ignore
from PySide6.QtCore import QTimer # type: ignore

# Importing program files
from Application.libs.Logging.logging import Logging
from Application.application import Application

# Create instance of Logging
logger = Logging()

# Save printf method
printf = logger.log

# Starting info message
printf(msg="Starting WebScope...", status="INFO")

# Create signal for canceling (Ctrl + C)
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Main running function main
def main() -> None:
    # Info print
    printf(msg="Running main function...", status="INFO")

    # Init application
    application = Application()

    # Execute applcation
    sys.exit(application.exec())

    # Set Qt timer 
    timer = QTimer()
    timer.start(100)
    timer.timeout.connect(lambda: None)

    # Close file
    file.close()

# Main block
if __name__ == "__main__":
    # Try block for cathcing exceptions
    try:
        # Running main function
        main()
    except Exception as e:
        # Print info about error
        printf(status="ERROR", msg="")

        # Print exception
        traceback.print_exception(type(e), e, e.__traceback__)
    except KeyboardInterrupt:
        # Exit if keyboard interrupt
        sys.exit(0)
