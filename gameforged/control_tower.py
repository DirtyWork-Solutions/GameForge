"""


"""

from pyutile.reporting.logged import log as LOG

# Dictionary of error codes and their descriptions
ERR_CODE_DICT = {
    0: "Unknown error",
    1: "Invalid input",
    2: "Invalid output",
    3: "Invalid operation",
    4: "Invalid state",
    5: "Invalid configuration",
    6: "Invalid request",
    7: "Invalid response",
    8: "Invalid format",
    9: "Invalid data",
    10: "Invalid parameter",
    11: "Invalid argument",
    12: "Invalid value",
    13: "Invalid type",
    14: "Invalid class",
    15: "Invalid method",
    16: "Invalid function",
    17: "Invalid module",
    18: "Invalid package",
    19: "Invalid library",
    20: "Invalid system",
    21: "Invalid environment",
    22: "Invalid platform",
    23: "Invalid version",
    24: "Invalid license",
    25: "Invalid permission",
    26: "Invalid access",
    27: "Invalid path",
    28: "Invalid file",
    29: "Invalid directory",
    30: "Invalid resource",
    31: "Invalid reference",
    32: "Invalid pointer",
    33: "Invalid index",
    34: "Invalid key",
    35: "Invalid name",
    36: "Invalid title",
    37: "Invalid description",
    38: "Invalid label",
    39: "Invalid tag",
    40: "Invalid attribute",
    41: "Invalid property",
    42: "Invalid field",
    43: "Invalid column",
    44: "Invalid row",
    45: "Invalid record",
    46: "Invalid data structure",
    47: "Invalid data format",
    48: "Invalid data model",
    49: "Invalid data type",
    50: "Invalid data class",
    51: "Invalid data object",
    52: "Invalid data value",
    53: "Invalid data range",
    54: "Invalid data domain",
    55: "Invalid data set",
    56: "Invalid data source",
    57: "Invalid data sink",
    58: "Invalid data stream",
    59: "Invalid data packet",
    60: "Invalid data block",
}

class GameForgedException(Exception):
    """
    Base exception class for GameForged.
    """

    def __init__(self, message: str, error_code: int = None, logged: bool = True, log_lvl: str = 'error'):
        """
        Initialize the exception with a message and an optional error code.

        """
        super().__init__(message)
        # Set the error code if it is valid, otherwise default to 0
        if error_code is None:
            self.error_code = -1
        else:
            self.error_code = error_code
        if logged:
            if error_code is None or error_code == -1:
                self.log_error(message)
            else:
                self.log_error(message, error_code)

    def log_error(self, message: str, error_code: int = None, lvl: str = None):
        """
        Log the error message with an optional error code.
        """
        #
        if lvl is None:
            lvl = 'error' if error_code else 'warning'
        #
        if error_code == -1:
            LOG.warning(f"Error {error_code}: {message}")
        else:
            LOG.warning(message)

    def __str__(self):
        """
        Return a string representation of the error, including the error code if available.
        """
        if self.error_code:
            return f"[Error {self.error_code}] {super().__str__()}"
        return super().__str__()


class Controller:  # TODO: Implement the controller class
    def __init__(self):
        LOG.warning("Controller functioality not implemented yet")
