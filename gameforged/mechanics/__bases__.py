"""
This module provides Base Classes for *all* **game theory** mechanics; such as *players* or *strategies*.
"""

from abc import ABC, abstractmethod
from gameforged.control_tower import LOG as log


class GameTheoryMechanic(ABC):
    """
    Identifying base class for a mechanics of game theory (e.g. *players* or *strategies*)
    """

    @abstractmethod
    def __init__(self):
        self.mechanic_name = 'game theory'

class BaseAgent(GameTheoryMechanic, ABC):
    """
    Abstract base class for decision-makers in a game.
    """
    mechanic_name = 'agents'
    mechanic_desc = 'decision-makers in a game'

    @abstractmethod
    def __init__(self):
        super().__init__()
        self._is_simulated = False

class BaseGame(GameTheoryMechanic, ABC):
    """
    An *abstract base class* for a **game**; a Structured interaction involving players making strategic decisions.
    """

    mechanic_name = 'games'
    mechanic_desc = 'a structured interaction involving players making strategic decisions.'

    @abstractmethod
    def __init__(self):
        """
        Initialize the 'game' mechanics.
        """
        super().__init__()
        self._players = []

    @property
    def players(self):
        return self._players


class BasePayoff(GameTheoryMechanic, ABC):
    """
    Quantification of outcomes based on players' actions.
    """
    mechanic_name = 'payoffs'
    mechanic_desc = 'quantification of outcomes based on players\' actions'

    @abstractmethod
    def __init__(self):
        super().__init__()


class BaseStrategy(GameTheoryMechanic, ABC):
    """

    """

    mechanic_name = 'strategies'

    @abstractmethod
    def __init__(self):
        super().__init__()


class BaseAction(GameTheoryMechanic, ABC):
    """

    """

    mechanic_name = 'actions'

    @abstractmethod
    def __init__(self):
        super().__init__()


class BaseInformation(GameTheoryMechanic, ABC):
    """

    """
    @abstractmethod
    def __init__(self):
        super().__init__()


class BaseTurn(GameTheoryMechanic, ABC):
    """

    """

    mechanic_name = 'turns'

    @abstractmethod
    def __init__(self):
        super().__init__()
