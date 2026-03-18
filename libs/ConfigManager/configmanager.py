# configmanager.py

# This modules are used for managing settings and other configuration
import json
import sys
import os

# Main class Config:
class Config:
    def __init__(self, parent):
        # Save parent 
        self.app = parent

        # Defautl settings
        self.defautl_config = {
            
        }

        # Config folder path
        self.config_dir = "Application/Config"

        # Condif file path
        self.config_file = "Application/Config/config.json" 

        # Check if config folder exists
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)

        # Check if config file exists
        if not os.path.exists(self.config_file):
            with open(self.config_file, "w") as config:
                json.dump(self.defautl_config, config, indent=4)