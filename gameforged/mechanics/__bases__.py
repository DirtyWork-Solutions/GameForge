"""
Base classes for game mechanic components
"""

from abc import ABC

class GameTheoryMechanic(ABC):
    pass

class BaseAgent(GameTheoryMechanic, ABC):
    pass

class BaseGame(GameTheoryMechanic, ABC):
    pass

class BasePayoff(GameTheoryMechanic, ABC):
    pass


class BaseStrategy(GameTheoryMechanic, ABC):
    pass

class BaseAction(GameTheoryMechanic, ABC):
    pass

class BaseInformation(GameTheoryMechanic, ABC):
    pass

class BaseTurn(GameTheoryMechanic, ABC):
    pass
