"""
This module defines how payoffs are calculated and distributed in a game, 
including deterministic, probabilistic, and adaptive payoffs.


**Key Components:**

- BasePayoff (Abstract Base Class):  *Defines the general structure for payoff calculation.*
- DeterministicPayoff:  *Fixed reward distribution based on a payoff matrix.*
- ProbabilisticPayoff:  *Payoffs influenced by probability distributions.*
- EvolutionaryPayoff:  *Payoffs that change over time based on player actions.*
- PayoffMatrix:  *A structured approach for defining game payoffs.*


**Features:**

- Supports different payoff structures for diverse game types.
- Enables modeling of evolving payoffs influenced by past moves.
- Provides utility functions for expected value calculations.


**Usage:**

This module is used for defining the reward structures in a game. 
Payoff types can be customized based on game design requirements.
"""

from typing import Dict, Tuple

from gameforged.mechanics.__bases__ import BasePayoff
from gameforged.control_tower import Controller

log = Controller.logger

class DeterministicPayoff(BasePayoff):
    """Fixed reward distribution based on a payoff matrix."""

    def __init__(self, matrix: Dict[Tuple, float]):
        self.matrix = matrix

    def get_payoff(self, strategies: Tuple):
        """Retrieves deterministic payoffs for a given strategy profile."""
        return self.matrix.get(strategies, 0.0)


class ProbabilisticPayoff(BasePayoff):
    """
    Payoffs influenced by probability distributions.
    """

    def __init__(self, matrix: Dict[Tuple, Tuple[float, float]]):
        self.matrix = matrix

    def get_payoff(self, strategies: Tuple):
        """Retrieves probabilistic payoffs for a given strategy profile."""
        import random
        mean, stddev = self.matrix.get(strategies, (0.0, 0.0))
        return random.gauss(mean, stddev)


class EvolutionaryPayoff(BasePayoff):
    """
    Payoffs that change over time based on player actions.
    """

    def __init__(self, initial_matrix: Dict[Tuple, float]):
        self.matrix = initial_matrix
        self.history = []

    def get_payoff(self, strategies: Tuple):
        """Retrieves evolving payoffs for a given strategy profile."""
        return self.matrix.get(strategies, 0.0)

    def update_payoff(self, strategies: Tuple, new_payoff: float):
        """Updates the payoff for a given strategy profile."""
        self.matrix[strategies] = new_payoff
        self.history.append((strategies, new_payoff))

class PayOffMatrix(BasePayoff):
    """
    Encapsulates payoffs as a matrix for extensibility.
    """

    def __init__(self, matrix: Dict[Tuple, Tuple]):
        self.matrix = matrix

    def get_payoff(self, strategies: Tuple):
        """Retrieves payoffs for a given strategy profile."""
        return self.matrix.get(strategies, (0, 0))
