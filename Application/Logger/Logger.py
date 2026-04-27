# Logger.py

from datetime import datetime
import threading
import os

from Application.AppContext import ctx

# Default configuration
DEFAULT_CONFIG = {
    "cb_console_time": "Yes",
    "cb_console_colors": "Yes",
    "btn_console_info": True,
    "btn_console_warning": True,
    "btn_console_success": True,
    "btn_console_error": True,
    "btn_console_debug": False,
    "cb_file_enabled": "Yes",
    "btn_file_info": False,
    "btn_file_warning": False,
    "btn_file_success": False,
    "btn_file_error": True,
    "btn_file_debug": False,
    "sb_file_rotation": 10,
    "sb_file_retention": 7,
    "le_file_path": "./Logs",
    "cb_file_compression": "zip"
}

class Logger:

    # Logs dir
    DEFAULT_LOG_DIR = "Logs"
    
    # Logs filepath
    DEFAULT_LOG_FILE = "app.log"

    # Level colors
    LEVEL_COLORS = {
        "INFO": "\033[94m",    # Light blue
        "WARN": "\033[93m",    # Yellow
        "SUCCESS": "\033[92m", # Green
        "ERROR": "\033[91m",   # Red
        "DEBUG": "\033[95m",   # Magenta
        "CRITICAL": "\033[1;41;97m", # Bold white
        "RESET": "\033[0m"     # Reset
    }
    
    def __init__(self, config:dict) -> None:
        # Log file handling and lock threads
        self.log = None
        self.lock = threading.Lock()

        # Create paths
        self.log_dir = config.get("le_file_path", DEFAULT_CONFIG.get("le_file_path", self.DEFAULT_LOG_DIR))
        self.log_path = os.path.join(self.log_dir, self.DEFAULT_LOG_FILE)

        # Start
        self.update(config)
        
    # Writing to console 
    def _cout(self, level, msg, func="", row="", filename="") -> None:  
        # Get timestamp and colors      
        timestamp = datetime.now().strftime("%H:%M:%S") if self.time else ""
        color = self.LEVEL_COLORS.get(level, "")
        reset = self.LEVEL_COLORS["RESET"]
        
        # Format message
        if self.colored:
            path = f"{filename}:{func}:{self.LEVEL_COLORS['WHITE_BOLD']}{row}{reset}"
            formatted_msg = f"{self.LEVEL_COLORS['GRAY']}{timestamp}{reset} {color}{level:^10}{reset} {path} - {msg}"
        else:
            formatted_msg = f"{timestamp} {level:^10} {filename}:{func}:{row} - {msg}"
        
        # Print to console
        print(formatted_msg)
    
    # Writing to file
    def _fout(self, level, msg, func="", row="", filename="") -> None:
        # Timestamp, path and msg
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") if self.time else ""
        path = f"{filename}:{func}:{row}"
        formatted_msg = f"{timestamp} {level:^10} {path} - {msg}\n"
        
        # Log to file
        try:
            self.log_file.write(formatted_msg)
            self.log_file.flush()
        except OSError:
            pass

    # Log to file and console
    def _log_generic(self, level, msg, is_exception=False):
        # Get caller
        caller = self._get_caller_info()
        
        # Lock threads
        with self.lock:
            # Cout to console
            if self.c_levels.get(level, False):
                self._cout(level, msg, **caller)
            
            # Fout to file
            if self.log_file and self.f_levels.get(level, False):
                self._fout(level, msg, **caller)
        self._cout("DEBUG", msg)
        if self.log:
            self._fout("DEBUG", msg)

    # Public logging methods
    def info(self, msg): self._log_generic("INFO", msg)
    def warn(self, msg): self._log_generic("WARN", msg)
    def success(self, msg): self._log_generic("SUCCESS", msg)
    def debug(self, msg): self._log_generic("DEBUG", msg)
    def error(self, msg): self._log_generic("ERROR", msg)
    def critical(self, exception):
        # Get details and log
        details = self._error_details(exception)
        self._log_generic("CRITICAL", details)

    # Get info about calling
    @staticmethod
    def _get_caller_info():
        import sys

        try:
            frame = sys._getframe(3)

            # Get filename, func and row
            return {
                "filename": os.path.basename(frame.f_code.co_filename),
                "func": frame.f_code.co_name,
                "row": frame.f_lineno
            }
        except Exception:
            # Return defaults
            return {"filename": "unknown", "func": "unknown", "row": 0}
        
    # Get error details
    @staticmethod
    def _error_details(exception) -> dict:
        import traceback
        import json
        import sys

        # Full traceback of error
        full_traceback = traceback.format_exc()
        
        # Error location
        _, _, exc_tb = sys.exc_info()
        tb_last = traceback.extract_tb(exc_tb)[-1] if exc_tb else None
        
        # Details dictonary
        details = {
            # Type and message
            "type": type(exception).__name__,
            "message": str(exception),
            
            # Localize error
            "file": tb_last.filename if tb_last else "Unknown",
            "line": tb_last.lineno if tb_last else "N/A",
            "function": tb_last.name if tb_last else "N/A",
            "code": tb_last.line if tb_last else "N/A",
            
            # Full trackeback
            "full_traceback": "\n" + full_traceback,

            # Extra info
            "extra_info": None
        }

        # Specific errors data
        if isinstance(exception, OSError):
            details["extra_info"]["errno"] = exception.errno
            details["extra_info"]["path"] = exception.filename

        # Format details
        json_string = json.dumps(details, indent=4, ensure_ascii=False)

        ident = " " * 6

        clean_json = json_string.replace('\\n', '\n' + ident)
        clean_json = clean_json.replace('\\"', '"')

        return clean_json

    # Update logger
    def update(self, config:dict) -> None:
        if self.log:
            # Close log
            try:
                self.log.close()
            except OSError:
                pass
                
            self.log = None
        
        # Get c_levels and f_levels
        self.c_levels = {
            "INFO": config["btn_console_info"],
            "WARN": config["btn_console_warning"],
            "SUCCESS": config["btn_console_success"],
            "ERROR": config["btn_console_error"],
            "DEBUG": config["btn_console_debug"],
            "CRITICAL": True
        }

        if config.get("cb_file_enabled") == "Yes":
            # Set levels for file logging
            self.f_levels = {
                "INFO": config["btn_file_info"],
                "WARN": config["btn_file_warning"],
                "SUCCESS": config["btn_file_success"],
                "ERROR": config["btn_file_error"],
                "DEBUG": config["btn_file_debug"],
                "CRITICAL": True
            }

            # File handling
            try:
                # Check logging directory
                if self.log_dir:
                    os.makedirs(self.log_dir, exist_ok=True)
                self.log = open(self.log_path, "a", encoding="utf-8")
            except OSError as e:
                self.critical(e)
                self.log = None

        else:
            self.f_levels = {
                "INFO": False,
                "WARN": False,
                "SUCCESS": False,
                "ERROR": False,
                "DEBUG": False,
                "CRITICAL": True
            }

        # Get time and colors
        self.time = config.get("cb_console_time") == "Yes"
        self.colored = config.get("cb_console_colors") == "Yes"

        # Log init
        self.info("Logger initialized")

# Init logger
logger = Logger(ctx.config.get("LoggingPage", DEFAULT_CONFIG))

