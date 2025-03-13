"""
This module provides different decision-making strategies, including 
pure, mixed, adaptive, and deceptive strategies.


**Key Components:**

- BaseStrategy (Abstract Base Class): Defines the interface for player strategies.
- PureStrategy: A static strategy where a player always makes the same move.
- MixedStrategy: A probabilistic strategy where players choose moves based on weighted probabilities.
- AdaptiveStrategy: A learning-based strategy that evolves over time.
- DeceptiveStrategy: A strategy that incorporates bluffing and misdirection.
- GraphDecisionStrategy: A strategy based on decision trees or game graphs.



**Features:**

- Supports AI-driven strategy selection and optimization.
- Allows strategies to adapt based on opponent behavior.
- Enables bluffing and deception mechanisms for psychological gameplay.



**Usage:**

This module should be used to assign strategies to AI players. 
Developers can extend strategies or integrate them with reinforcement learning models.
"""

from gameforged.mechanics.__bases__ import BaseStrategy, BaseAction
from gameforged.control_tower import Controller

log = Controller.logger

class PureStrategy(BaseStrategy):
    """
    A static strategy where a player always makes the same move.
    """

    def __init__(self, name: str = "Pure Strategy", uid: str = None):
        super().__init__(name, uid)



class MixedStrategy(BaseStrategy):
    """
    A probabilistic strategy where players choose moves based on weighted probabilities.
    """

    def __init__(self):
        super().__init__()



class AdaptiveStrategy(BaseStrategy):
    """
    A learning-based strategy that evolves over time.
    """

    def __init__(self):
        super().__init__()



class DeceptiveStrategy(BaseStrategy):
    """
    A strategy that incorporates bluffing and misdirection.
    """

    def __init__(self):
        super().__init__()



class GraphDecisionStrategy(BaseStrategy):
    """
    A strategy based on decision trees or game graphs.
    """

    def __init__(self):
        super().__init__()


class StrategyBuilder:
    """
    A builder class for creating strategies.

    Steps:

    """

    def __init__(self, template: BaseStrategy | None = None):
        self._strategy = None

    def set_strategy(self, strategy: BaseStrategy):
        self._strategy = strategy


    def check_build(self, hard_fail: bool = False) -> bool:
        """
        Check if the strategy is ready to be built.

        :param hard_fail: bool - raise an appropriate exception if checks fail? **Default is False.**

        :return: bool - True if the strategy is ready to be built, False otherwise. *Nothing is returned with hard_fail=True*.

        :raises AssertionError: If the strategy is not ready to be built *and* hard_fail=True.
        """
        if not hard_fail:
            log.error("Builder and it's internal build check are not yet implemented. Returning False.")
            return False
        else:
            raise NotImplementedError("Strategy Builder (incl. build checks) are not yet implemented "
                                      "and the check was set to hard fail.")

    def build(self):
        if self._strategy:
            log.success(f"{self._strategy}")
            return self._strategy
        else:
            log.error("No strategy set. Please set a strategy before building.")
            return None

class Strategy(BaseStrategy):
    """"""
    def __init__(self, strategy: BaseStrategy):
        self._strategy = None

    def create(self):
        log.error("Interface not implemented yet.")

if __name__ == '__main__':
    plan = StrategyBuilder()
    ready = plan.check_build()
    print(ready)