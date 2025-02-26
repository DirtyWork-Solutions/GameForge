"""
This module manages player interactions within the game, including human, AI, 
and negotiation-based players.


**Key Components:**

- BaseAgent (Abstract Base Class): Defines common attributes and methods for players.
- HumanPlayer: A player controlled by human input.
- AIPlayer: A player controlled by an AI strategy.
- NegotiationPlayer: A player with additional interaction mechanisms such as trade and alliances.
- PlayerGroup: A structure for managing teams or collective strategies.

**Features:**

- Supports AI and human-controlled players with different decision-making approaches.
- Enables negotiation-based gameplay for trading, alliances, and betrayals.
- Allows behavioral tracking for advanced analytics (e.g., detecting player tendencies).


**Usage:**

This module should be used to define players in a game and assign them roles, strategies, 
and decision-making mechanisms. AI players can integrate with the strategies' module.
"""
from abc import ABC

from gameforged.mechanics.__bases__ import BaseAgent
from gameforged.control_tower import LOG as log


class SimulatedAgent(BaseAgent):
    """
    Mix-in class for agents that are simulated by the game engine.


    """
    def __init__(self):
        super().__init__()
        self.simulation_state = None
        self._is_simulated = True

    @property
    def is_simulated(self) -> bool:
        return self._is_simulated



    def start_simulation(self):
        self.simulation_state = 'running'
        log.info(f"Simulation started with speed {self.simulation_speed} and accuracy {self.simulation_accuracy}")

    def pause_simulation(self):
        self.simulation_state = 'paused'
        log.info("Simulation paused")

    def stop_simulation(self):
        self.simulation_state = 'stopped'
        log.info("Simulation stopped")

    def update_simulation(self):
        if self.simulation_state == 'running':
            # Update the simulation state here
            log.info("Simulation updated")

class HumanPlayer(BaseAgent):
    """
    A Player representing a human-controlled agent.
    """
    def __init__(self):
        super().__init__()


class AIPlayer(BaseAgent, SimulatedAgent):
    """
    A Player representing an AI-controlled agent.
    """
    def __init__(self):
        super().__init__()


class NegotiationPlayer(BaseAgent):
    """
    Mix-in class?
    """

    def __init__(self):
        super().__init__()

