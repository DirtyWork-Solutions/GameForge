"""
This module provides different decision-making strategies, including 
pure, mixed, adaptive, and deceptive strategies.

**Key Components:**
- Strategy (Abstract Base Class): Defines the interface for player strategies.
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
