"""
Module for extending the functionality of the gameforged package.
"""

from gameforged.control_tower import INTERFACES as interfaces
from gameforged.utilities.data_io import save_data, load_data
from gameforged.errors import *

# TODO: Implement extension system here

class ExtensionEngine:
    def __init__(self):
        self._extensions = {}

    def startup(self):  # # TODO: Implement power-up for extensions engine
        pass

    def shutdown(self):  # TODO: Implement power-down for extensions engine
        pass