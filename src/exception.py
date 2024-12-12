import sys
from src.logger import logging

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Constructs a detailed error message with file name, line number, and error message.

    Args:
        error (Exception): The exception object.
        error_detail (sys): System module for accessing traceback information.

    Returns:
        str: Detailed error message.
    """
    _, _, exc_tb = error_detail.exc_info()  # exc_tb gives info about error location and type
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "Unknown"
        line_number = "Unknown"
        
    error_message = f"Error occurred in python script name [{file_name}] line number [{line_number}] error message [{str(error)}]."
    return error_message

class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        """
        Custom exception class that provides detailed error information.

        Args:
            error_message (Exception): The original exception message.
            error_detail (sys): System module for accessing traceback information.
        """
        super().__init__(str(error_message))  # Ensures base Exception initialization
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message
