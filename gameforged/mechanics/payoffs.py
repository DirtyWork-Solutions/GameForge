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

from gameforged.mechanics.__bases__ import BasePayoff


class PayOffMatrix:
    pass