"""


"""

from bedrocked.reporting.reported import logger as LOG
from gameforged.utilities.interfaces import Interfaces
from gameforged.utilities.data_io import save_data, load_data
from gameforged.errors import *

###
## GLOBALS -
###
#
# Singleton instance of the Interfaces class
INTERFACES = Interfaces()
from gameforged.errors import ERR_CODE_DICT


class Controller:  # TODO: Implement the controller class
    """

    """
    logger = LOG
    interfaces = INTERFACES

    @property
    def toolbox(self):
        return Toolbox()


class Toolbox:  # TODO: Make a singleton class
    """

    """

    def __init__(self):
        pass

    @property
    def controller(self):
        return engine

engine = Controller()
