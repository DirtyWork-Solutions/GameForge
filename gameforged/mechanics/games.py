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

from gameforged.mechanics.__bases__ import BaseGame, BaseTurn
from gameforged.control_tower import log

class SequentialGame(BaseGame):
    """
    A turn-based game with players acting in a fixed order.
    """
    def __init__(self):
        super().__init__()
        log.debug("Sequential Game Initialized")


class SimultaneousGame(BaseGame):
    """

    """

    def __init__(self):
        super().__init__()
        log.debug("Simultaneous Game Initialized")

class AdaptiveGame(BaseGame):
    """
    A game where all players act simultaneously.
    """

    def __init__(self):
        super().__init__()
        log.debug("Adaptive Game Initialized")

class GameState:
    """

    """

    def __init__(self):
        super().__init__()
        log.debug("Game State Initialized")


class Game:
    def __init__(self):
        self._game = None

    def create_game(self, game_type: str):
        if game_type == "sequential":
            self._game = SequentialGame()
        elif game_type == "simultaneous":
            self._game = SimultaneousGame()
        elif game_type == "adaptive":
            self._game = AdaptiveGame()
        else:
            log.error("Invalid game type. Please choose from 'sequential', 'simultaneous', or 'adaptive'.")

    def start_game(self):
        if self._game:
            try:
                self._game.start()
            except Exception as e:
                log.error(f"Error starting game: {e}")
        else:
            log.error("No game created. Please call create_game() first.")

    def end_game(self):
        if self._game:
            self._game.end()
        else:
            log.error("No game created. Please call create_game() first.")