from abc import ABC


class BaseInterface(ABC):  # TODO: Create the base class for interfaces
    """
    """
    pass

class ProgrammaticInterface(BaseInterface):  # TODO: Implement a programmatic interface
    """
    """
    pass

class CommandInterface(BaseInterface):
    """
    """
    pass

class WebInterface(BaseInterface):
    """
    """
    pass

class InterfaceManager:
    pass


class Interfaces:  # TODO: Turn into a singleton
    """

    """

    def __init__(self):
        """

        """
        self._available_interfaces = []



    @property
    def active_interfaces(self) -> int:
        """

        """
        # TODO: Implement count of active interfaces
        return len(self._available_interfaces)
