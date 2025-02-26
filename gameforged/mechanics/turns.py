"""
This module provides a framework for handling different types of turn structures 
in a game, including discrete, real-time, and multiphase turns.


**Key Components:**

- Turn (Abstract Base Class): Defines the basic interface for a turn.
- DiscreteTurn: Traditional turn-based structure with a defined order.
- RealTimeTurn: Time-constrained, continuously updating game turns.
- MultiPhaseTurn: A turn system that divides execution into distinct phases.
- TurnManager: A utility class to handle turn sequencing and scheduling.


**Features:**

- Supports turn execution customization (synchronous, asynchronous, or timed).
- Allows turn interruptions and event-based modifications.
- Provides a centralized turn manager for complex games.


**Usage:**

Use this module to define and control the flow of turns in a game.
The TurnManager can be used to orchestrate different types of turn-based logic.
"""

from gameforged.mechanics.__bases__ import BaseTurn
from gameforged.control_tower import LOG as log
