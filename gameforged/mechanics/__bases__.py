"""
Base classes for game mechanic components
"""

from abc import ABC, abstractmethod


class GameTheoryMechanic(ABC):
    """
    Identifying base class for a mechanics of game theory (e.g. *players* or *strategies*)
    """

    @abstractmethod
    def __init__(self):
        self.mechanic_name = 'game theory'

class BaseAgent(GameTheoryMechanic, ABC):
    """
    Abstract base class for
    """
    @abstractmethod
    def __init__(self):
        super().__init__()
        self.mechanic_name = 'agents'



class BaseGame(GameTheoryMechanic, ABC):
    """
    Abstract base class for
    """
    @abstractmethod
    def __init__(self):
        super().__init__()
        self.mechanic_name = 'games'


class BasePayoff(GameTheoryMechanic, ABC):
    @abstractmethod
    def __init__(self):
        super().__init__()
        self.mechanic_name = 'payoffs'


class BaseStrategy(GameTheoryMechanic, ABC):
    @abstractmethod
    def __init__(self):
        super().__init__()
        self.mechanic_name = 'strategies'


class BaseAction(GameTheoryMechanic, ABC):
    @abstractmethod
    def __init__(self):
        super().__init__()
        self.mechanic_name = 'actions'


class BaseInformation(GameTheoryMechanic, ABC):
    @abstractmethod
    def __init__(self):
        super().__init__()
        self.mechanic_name = 'information'


class BaseTurn(GameTheoryMechanic, ABC):
    @abstractmethod
    def __init__(self):
        super().__init__()
        self.mechanic_name = 'turns'
