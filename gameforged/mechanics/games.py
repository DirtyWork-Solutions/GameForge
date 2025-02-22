"""
This module defines the fundamental structure of a game, including different types of games (e.g., sequential,
simultaneous, adaptive) and their state management.


**Key Components:**

- BaseGame (Abstract Base Class): Defines the fundamental game lifecycle.
- SequentialGame: A turn-based game with players acting in a fixed order.
- SimultaneousGame: A game where all players act simultaneously.
- AdaptiveGame: A dynamic game where rules and strategies evolve.
- GameState: Encapsulates the board state, player scores, and history.


**Features:**

- Provides base implementations that can be extended for custom game types.
- Supports dynamic rule modifications in AdaptiveGame.
- Includes a structured state management system.


**Usage:**

This module serves as the foundation for defining different game structures and should be used as a base when
implementing specific game mechanics.
"""

from gameforged.mechanics.__bases__ import BaseGame
