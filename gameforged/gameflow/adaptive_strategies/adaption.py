from abc import ABC, abstractmethod

from gameforged.control_tower import Controller

log = Controller.logger
from gameforged.mechanics.__bases__ import BaseStrategy


class AdaptiveStrategyManager:  # TODO: Create this manager
    """
    Central manager for adapting strategies across players/agents.
    """
    def __init__(self):
        log.debug("Adaptive strategy manager initialized.")


class BaseStrategyAdjuster(ABC):
    """
    Provides a template for adjusting specific types of strategies (e.g., economic, political).
    """
    def __init__(self):
        pass

    @abstractmethod
    def adjust(self, current_strategy, game_state) -> BaseStrategy:
        """
        Abstract method for computing a new strategy.
        """
        pass


class EconomicStrategyAdjuster(BaseStrategyAdjuster):
    """
    Implements adjustments for economic decisions.
    """
    pass


class PoliticalStrategyAdjuster(BaseStrategyAdjuster):
    """
    Adjusts strategies based on political shifts or regulatory changes.
    """
    pass
