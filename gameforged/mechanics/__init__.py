"""
The mechanics subpackage serves as the core of the GameForge ecosystem. It provides the foundational components for
constructing game environments, managing turn-based or real-time play, defining player roles, setting up payoff
structures, and implementing strategic decision-making. The mechanics layer is the engine that drives the simulation’s
basic logic, ensuring that every game scenario, regardless of complexity, is built upon a consistent and robust framework.

**Key Modules and Their Roles:**

game.py:
Contains the central game class that orchestrates the overall simulation. It sets up the initial game state, manages rounds or turns, and oversees the progression of the simulation.

turn.py:
Manages the sequencing of game rounds, including turn order, time progression, and synchronization between players’ actions. It supports both discrete and continuous turn mechanisms.

players.py:
Defines the player models, roles, and attributes. This module includes classes for human and AI players, managing their state, strategies, and interactions within the game environment.

payoffs.py:
Contains the logic for computing rewards, losses, and overall utility for players based on their decisions and game outcomes. It includes methods for dynamic adjustment of payoffs in response to evolving game conditions.

strategies.py:
Provides a framework for defining and evaluating strategies. It includes basic strategy patterns as well as interfaces for integrating more advanced, adaptive approaches from the AI modules.

information.py:
Focuses on modeling the distribution of information among players. It implements mechanisms for hidden, public, and asymmetric information, which are critical for scenarios involving signaling, bluffing, and incomplete knowledge.


**Intended Usage:**

The mechanics subpackage forms the core simulation environment upon which more advanced features (like those in GameFlow) are built. It establishes the basic rules, state management, and player interactions necessary for any game scenario, from simple turn-based puzzles to highly complex multi-agent simulations. Developers leverage these components to rapidly prototype game scenarios and ensure that advanced features have a solid and consistent operational foundation.

"""