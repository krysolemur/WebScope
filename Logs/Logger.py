# Logger.py

# Importing system modules
import logging
import sys

# Main class Logger
class Logger:

    # Init
    def __init__(self, levels:list, name:str) -> None:

        # Create logger with name
        self.logger = logging.getLogger(name)
        numeric_levels = [getattr(logging, l.upper()) for l in levels]
        self.logger.setLevel(min(numeric_levels))
        
        # Zabráníme duplikování handlerů, pokud se Logger inicializuje vícekrát
        if not self.logger.handlers:
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )

            # 1. Výstup do konzole
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

            # 2. Volitelný výstup do souboru (pokud je v settings/argumentech)
            # if log_file:
            #     file_handler = logging.FileHandler(log_file)
            #     file_handler.setFormatter(formatter)
            #     self.logger.addHandler(file_handler)
