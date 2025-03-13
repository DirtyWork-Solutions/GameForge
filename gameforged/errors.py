from pyutile.reporting.logged import log as LOG

# Dictionary of error codes and their descriptions
ERR_CODE_DICT = {
    0: {"msg": "Unknown error",
        "lvl": "error",
        "logged": True,
        "fatal": True,
        "exception_classes": ["GameForgedException"]
        },
    1: {"msg": "Invalid Input",
        "lvl": "error",
        "logged": True,
        "fatal": True,
        "exception_classes": ["GameForgedException"]
        },
    2: {"msg": "Invalid Output",
        "lvl": "error",
        "logged": True,
        "fatal": True,
        "exception_classes": ["GameForgedException"]
        },
    3: {"msg": "Invalid operation",
        "lvl": "error",
        "logged": True,
        "fatal": True,
        "exception_classes": ["GameForgedException"]
        },
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


class ErrorHandler:
    """
    Error handler class for GameForged.
    """
    CODE = ERR_CODE_DICT


class Error:
    """

    """

    def __init__(self,
                 code: int = None,
                 message: str = None,
                 output: str = None,
                 log: bool = True,
                 lvl: str = 'error',
                 classes: list = None,
                 fatal: bool = False):

        self.fatal = fatal
        self.classes = classes if classes else [GameForgedException]
        self.code = code

        #
        if code is None or code <= 0 or code >= 999999:
            self.code = 0
        elif code and code in ErrorHandler().CODE.keys():
            self.code = code
        else:
            self._code = 0

        @property
        def code(self):
            return self._code

        @property
        def full_code(self):
            return f"GF{self.code:}"

        @code.setter
        def code(self, value: int):
            if value is None or value <= 0 or value >= 999999:
                self._code = 0
            elif value and value in ErrorHandler().CODE.keys():
                self._code = value
            else:
                self._code = 0

        @full_code.setter
        def full_code(self, value: str | int):
            try:
                self._code = int(value)
            except Exception as e:
                self._code = 0

        #
        if message and message != '':
            self.message = message
        elif code in ERR_CODE_DICT.keys():
            self.message = self.load_message_code(code)
        else:
            self.message = self.load_message_code(code)

        #
        self.logged = log
        self.lvl = lvl.lower() if lvl.lower() in ['debug', 'info', 'warning', 'error', 'critical'] else 'error'



    def load_message_code(self, code=0):
        """

        :param code:
        :return:
        """
        print(code)
        if code:
            LOG.success(f"Loading error message for code: {code}")
            self._code = code
            self.message = ERR_CODE_DICT[self._code]
        elif code and code in ErrorHandler().CODE.keys():
            LOG.debug(f"Loading error message for code: {code}")
            self.message = ERR_CODE_DICT[code]["msg"]
        else:
            self.message = ERR_CODE_DICT[code]["msg"]

        return self.message

    def raise_error(self):
        """

        """
        if self.logged and self.is_fatal():
            LOG.critical(f"[FATAL ERROR] {self.code}: {self.message}")
        elif self.logged and self.lvl == 'error' and not self.is_fatal():
            LOG.error(f"[ERROR] {self.code}: {self.message}")
        elif self.logged and self.lvl == 'warning':
            LOG.warning(f"[WARNING] {self.code}: {self.message}")
        elif self.logged and self.lvl == 'info':
            LOG.info(f"[INFO] {self.code}: {self.message}")
        elif self.logged and self.lvl == 'success':
            LOG.success(f"[SUCCESS] {self.code}: {self.message}")
        elif self.logged and self.lvl == 'debug':
            LOG.debug(f"[DEBUG] {self.code}: {self.message}")
        else:
            LOG.exception(f"[EXCEPTION] {self.code}: {self.message}")

        if self.fatal:
            # Check for multiple exception classes
            if len(self.classes) > 1:
                # Dynamically create a new exception class that inherits from the specified classes
                exception_class = type('DynamicException', tuple(self.classes), {})
                raise exception_class(self.message)
            else:
                raise self.classes[0](self.message, self.code)




    def is_fatal(self):
            """"""
            if self.lvl in ['error', 'critical']:
                return True
            elif self.fatal:
                return True
            else:
                return False


class GameForgedException(Exception):
    """
    Base exception class for GameForged.
    """

    def __init__(self, message: str, error_code: int = None, logged: bool = False, lvl: str = 'error'):
        """
        Initialize the exception with a message and an optional error code.

        """
        super().__init__(message)
        # Set the error code if it is valid, otherwise default to 0
        if error_code is None and self.code is None:
            self.code = -1
        else:
            self.code = error_code
        #
        if logged:
            if error_code is None or error_code == -1:
                self.log_error(message)
            else:
                self.log_error(message, error_code)

            self.lvl = lvl if lvl.lower() in ['debug', 'info', 'warning', 'error', 'critical'] else 'error'

    def log_error(self, message: str, error_code: int = None, lvl: str = None):
        """
        Log the error message with an optional error code.
        """
        #
        if lvl is None:
            lvl = 'error' if error_code else 'warning'
        #
        if lvl.lower() in ['debug', 'info', 'warning', 'error', 'critical']:
            LOG.log(lvl.upper(), f"[Error {error_code}] {message}")

    def __str__(self):
        """
        Return a string representation of the error, including the error code if available.
        """
        if self.code:
            return f"[Error {self.code}] {super().__str__()}"
        return super().__str__()


class GameForgedError(GameForgedException):
    pass


