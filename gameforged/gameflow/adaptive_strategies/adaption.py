from abc import ABC, abstractmethod

from gameforged.control_tower import Controller

log = Controller.logger
from gameforged.mechanics.__bases__ import BaseStrategy



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
    def __init__(self, investment):
        super().__init__()
        self.investment = investment

    def adjust(self, current_strategy, game_state) -> BaseStrategy:
        # Example logic for adjusting economic strategy
        new_strategy = current_strategy.clone()
        if game_state.economic_conditions == "recession":
            new_strategy.investment -= 10
        elif game_state.economic_conditions == "boom":
            new_strategy.investment += 10
        log.debug(f"Economic strategy adjusted: {new_strategy}")
        return new_strategy


class PoliticalStrategyAdjuster(BaseStrategyAdjuster):
    """
    Adjusts strategies based on political shifts or regulatory changes.
    """

    def adjust(self, current_strategy, game_state) -> BaseStrategy:
        # Example logic for adjusting political strategy
        new_strategy = current_strategy.clone()
        if game_state.political_climate == "unstable":
            new_strategy.diplomacy -= 5
        elif game_state.political_climate == "stable":
            new_strategy.diplomacy += 5
        log.debug(f"Political strategy adjusted: {new_strategy}")
        return new_strategy


class AdaptiveStrategyManager:
    """
    Central manager for adapting strategies across players/agents.
    """
    def __init__(self):
        self.strategies = []
        log.debug("Adaptive strategy manager initialized.")

    def add_strategy(self, strategy: BaseStrategyAdjuster):
        """
        Adds a new strategy adjuster to the manager.
        """
        self.strategies.append(strategy)
        log.debug(f"Strategy {strategy.__class__.__name__} added.")

    def remove_strategy(self, strategy: BaseStrategyAdjuster):
        """
        Removes a strategy adjuster from the manager.
        """
        if strategy in self.strategies:
            self.strategies.remove(strategy)
            log.debug(f"Strategy {strategy.__class__.__name__} removed.")
        else:
            log.debug(f"Strategy {strategy.__class__.__name__} not found in the manager.")

    def list_strategies(self):
        """
        Lists all current strategy adjusters in the manager.
        """
        strategy_names = [strategy.__class__.__name__ for strategy in self.strategies]
        log.debug(f"Current strategies: {strategy_names}")
        return strategy_names

    def clear_strategies(self):
        """
        Clears all strategy adjusters from the manager.
        """
        self.strategies.clear()
        log.debug("All strategies cleared from the manager.")



    def adjust_strategies(self, game_state):
        """
        Adjusts all strategies based on the current game state.
        """
        for strategy in self.strategies:
            new_strategy = strategy.adjust(strategy, game_state)
            log.debug(f"Strategy {strategy.__class__.__name__} adjusted to {new_strategy}.")

    def find_strategy_by_name(self, strategy_name: str) -> BaseStrategyAdjuster | None:
        """
        Finds a strategy adjuster by its class name.
        """
        for strategy in self.strategies:
            if strategy.__class__.__name__ == strategy_name:
                log.debug(f"Strategy {strategy_name} found.")
                return strategy
        log.debug(f"Strategy {strategy_name} not found.")
        return None

    def strategy_exists(self, strategy_name: str) -> bool:
        """
        Checks if a strategy adjuster exists in the manager by its class name.
        """
        for strategy in self.strategies:
            if strategy.__class__.__name__ == strategy_name:
                log.debug(f"Strategy {strategy_name} exists in the manager.")
                return True
        log.debug(f"Strategy {strategy_name} does not exist in the manager.")
        return False

