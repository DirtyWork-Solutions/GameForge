"""
Handles the detection, scheduling, and execution of game-changing events such as crises, policy shifts, or unexpected
external shocks. These events serve as catalysts that force players and AI agents to re-evaluate strategies.
"""
from abc import ABC, abstractmethod
from gameforged.control_tower import LOG as log


class BaseEventTrigger(ABC):
    """
    Abstract class defining the interface for all event triggers.
    """

    @abstractmethod
    def check_conditions(self, game_state) -> bool:
        pass

    @abstractmethod
    def execute(self, game_state) -> None:
        pass

    @abstractmethod
    def get_impact(self) -> dict:
        pass

class TimedEventTrigger(BaseEventTrigger):
    """
    Triggers events based on in-game time or turn count.
    """
    pass

class ConditionalEventTrigger(BaseEventTrigger):
    """
    Triggers events when specific conditions in the game state are met.
    """
    pass

class RandomEventTrigger(BaseEventTrigger):
    """
    Introduces stochastic events with a given probability.
    """
    pass