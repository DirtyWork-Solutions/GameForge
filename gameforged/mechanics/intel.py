"""
This module defines how information is shared, hidden, or distorted 
among players in a game.

**Key Components:**
- InformationSet (Abstract Base Class): Defines the basic interface for information access.
- PerfectInformation: All players have full knowledge of the game state.
- ImperfectInformation: Some aspects of the game state are hidden.
- AsymmetricInformation: Different players have different levels of knowledge.
- MisinformationMechanic: Allows intentional distortion of information.

**Features:**
- Supports different levels of information asymmetry.
- Enables deception and strategic misinformation.
- Allows dynamic updates to player knowledge.

**Usage:**
Use this module to define how much information is visible to each player. 
It is especially useful for games with hidden roles or incomplete knowledge.
"""

from gameforged.mechanics.__bases__ import BaseInformation
