"""
This module provides computational methods and classes to compute, analyze, and evaluate different types of equilibria
in game-theoretic models. It includes solvers for Nash, Correlated, Bayesian, and Evolutionary equilibria, along with
tools for stability testing, dynamic equilibrium management, approximations, and handling network-based games. Popular
packages such as numpy and scipy are used for numerical computations and optimization.
"""

from gameforged.control_tower import log as logger

import numpy as np
from abc import ABC, abstractmethod
from scipy.optimize import linprog

from gameforged.mechanics.__bases__ import BaseGame, BaseStrategy, BaseAgent


# =============================================================================
# Dummy Game Classes for Demonstration Purposes
# =============================================================================
class Game(BaseGame):
    """
    Represents a simple normal-form game.

    Attributes:
        payoff_matrix (np.array): 2D array representing the payoff matrix.
        players (list): List of players' names.
    """

    def __init__(self, payoff_matrix, players):
        super().__init__()
        self.payoff_matrix = np.array(payoff_matrix)
        self.players = players

    def is_normal_form(self):
        # For demonstration, we assume the game is normal form.
        return True

    def get_deviations(self, strategy_profile):
        """
        Returns a dummy mapping of players to deviation payoffs.
        In a full implementation, this would compute the best response deviations.
        """
        return {player: np.random.rand() for player in self.players}

    def expected_payoff(self, player, strategy_profile):
        """
        Returns a dummy expected payoff for a player given a strategy profile.
        """
        return np.random.rand()


class BayesianGame(Game):
    """
    Extends Game to include incomplete information (beliefs).

    Attributes:
        beliefs (dict): Beliefs over player types.
    """

    def __init__(self, payoff_matrix, players: BaseAgent, beliefs):
        """

        :param payoff_matrix:
        :param players:
        :param beliefs:
        """
        super().__init__(payoff_matrix, players)
        self.beliefs = beliefs


class PopulationGame(Game):
    """
    Represents a game suitable for evolutionary analysis.
    """

    def fitness(self, player: BaseAgent, strategy_profile: BaseStrategy) -> float:
        """

        :param player:
        :param strategy_profile:
        :return:
        """
        """
        Returns a dummy fitness value for a given player's strategy.
        """
        return np.random.rand()


# =============================================================================
# Equilibrium Data Structure
# =============================================================================
class Equilibrium:
    """
    Represents an equilibrium state in a game.

    Attributes:
        strategy_profile (dict): Mapping from players to their strategies.
        stability_metric (float): A measure of how stable the equilibrium is.
    """

    def __init__(self, strategy_profile: BaseStrategy, stability_metric=1.0):
        self.strategy_profile = strategy_profile
        self.stability_metric = stability_metric

    def is_stable(self) -> bool:
        """Returns True if the equilibrium is considered stable."""
        return self.stability_metric >= 1.0

    def __repr__(self):
        return f"Equilibrium(strategy_profile={self.strategy_profile}, stability_metric={self.stability_metric})"


# =============================================================================
# Base Equilibrium Solver Interface
# =============================================================================
class EquilibriumSolver(ABC):
    """
    Abstract base class for equilibrium solvers.

    Methods:
        compute_equilibrium(game): Computes and returns an Equilibrium.
        is_equilibrium(strategy_profile, game): Checks if the strategy_profile is an equilibrium.
    """

    @abstractmethod
    def compute_equilibrium(self, game: BaseGame):
        pass

    @abstractmethod
    def is_equilibrium(self, strategy_profile: BaseStrategy, game: BaseGame) -> bool:
        pass


# =============================================================================
# Nash Equilibrium Solver
# =============================================================================
class NashEquilibriumSolver(EquilibriumSolver):
    """
    Computes Nash equilibria for normal-form games.
    Uses linear programming techniques (e.g., via scipy.optimize.linprog) for demonstration.
    """

    def compute_equilibrium(self, game):
        if game.is_normal_form():
            return self._compute_normal_form(game)
        else:
            # Fallback for non-normal form games
            return self._compute_normal_form(game)

    def is_equilibrium(self, strategy_profile, game):
        # Dummy check: ensure that no unilateral deviation yields higher payoff.
        deviations = game.get_deviations(strategy_profile)
        for player in game.players:
            current_payoff = game.expected_payoff(player, strategy_profile)
            if deviations[player] > current_payoff:
                return False
        return True

    def _compute_normal_form(self, game: BaseGame):
        """
        Computes a Nash equilibrium for a normal-form game.
        For simplicity, we assume a two-player zero-sum game and use linprog.
        """
        try:
            num_strategies = game.payoff_matrix.shape[1]
            # Objective: minimize the sum of probabilities (dummy objective)
            c = np.ones(num_strategies)
            # Constraints: -payoff_matrix * x <= -1 (dummy constraints)
            A = -game.payoff_matrix
            b = -np.ones(game.payoff_matrix.shape[0])
            bounds = [(0, None) for _ in range(num_strategies)]
            res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
            if res.success:
                # Normalize the strategy vector
                strategy = res.x / np.sum(res.x)
                # For demonstration, assign same strategy for both players
                strategy_profile = {game.players[0]: strategy.tolist(),
                                    game.players[1]: np.ones(num_strategies) / num_strategies}
                eq = Equilibrium(strategy_profile, stability_metric=1.0)
                logger.debug(f"Nash equilibrium computed: {eq}")
                return eq
            else:
                logger.error("Failed to compute Nash equilibrium using linprog.")
                raise Exception("Nash equilibrium computation failed.")
        except Exception as e:
            logger.exception("Exception in _compute_normal_form:")
            raise e


# =============================================================================
# Correlated Equilibrium Solver
# =============================================================================
class CorrelatedEquilibriumSolver(EquilibriumSolver):
    """
    Computes correlated equilibria using a linear programming formulation.
    In this demonstration, a dummy equilibrium is returned.
    """

    def compute_equilibrium(self, game):
        # For demo purposes, generate a random strategy profile with Dirichlet distribution.
        strategy_profile = {player: np.random.dirichlet(np.ones(3)).tolist() for player in game.players}
        eq = Equilibrium(strategy_profile, stability_metric=1.0)
        logger.debug(f"Correlated equilibrium computed: {eq}")
        return eq

    def is_equilibrium(self, strategy_profile, game):
        deviations = game.get_deviations(strategy_profile)
        for player in game.players:
            if deviations[player] > game.expected_payoff(player, strategy_profile):
                return False
        return True


# =============================================================================
# Bayesian Nash Equilibrium Solver
# =============================================================================
class BayesianNashSolver(EquilibriumSolver):
    """
    Computes Bayesian Nash equilibria for games with incomplete information.
    This is demonstrated via a dummy iterative best response.
    """

    def compute_equilibrium(self, game):
        strategy_profile = {player: np.random.rand() for player in game.players}
        eq = Equilibrium(strategy_profile, stability_metric=1.0)
        logger.debug(f"Bayesian Nash equilibrium computed: {eq}")
        return eq

    def is_equilibrium(self, strategy_profile, game):
        deviations = game.get_deviations(strategy_profile)
        for player in game.players:
            if deviations[player] > game.expected_payoff(player, strategy_profile):
                return False
        return True


# =============================================================================
# Evolutionary Stable Strategy (ESS) Solver
# =============================================================================
class EvolutionaryStableStrategySolver(EquilibriumSolver):
    """
    Computes evolutionarily stable strategies (ESS) using replicator dynamics.
    This dummy implementation returns a random equilibrium.
    """

    def compute_equilibrium(self, game: BaseGame):
        strategy_profile = {player: np.random.rand() for player in game.players}
        eq = Equilibrium(strategy_profile, stability_metric=1.0)
        logger.debug(f"Evolutionarily stable strategy computed: {eq}")
        return eq

    def is_equilibrium(self, strategy_profile, game: BaseGame):
        deviations = game.get_deviations(strategy_profile)
        for player in game.players:
            if deviations[player] > game.expected_payoff(player, strategy_profile):
                return False
        return True


# =============================================================================
# Additional Components
# =============================================================================
class PerturbedEquilibrium:
    """
    Tests the stability of a given equilibrium under small random perturbations.

    Attributes:
        equilibrium (Equilibrium): The equilibrium to test.
        perturbation_scale (float): The standard deviation of the perturbation noise.
    """

    def __init__(self, equilibrium, perturbation_scale=0.05):
        self.equilibrium = equilibrium
        self.perturbation_scale = perturbation_scale

    def test_stability(self, game) -> bool:
        """
        Applies small random perturbations to the equilibrium's strategy profile and
        checks if it remains an equilibrium.

        :param game: An instance of Game.
        :return: (**Boolean**) indicating if the perturbed equilibrium still holds.

        :raises
        """
        perturbed_profile = {}
        for player, strategy in self.equilibrium.strategy_profile.items():
            strategy = np.array(strategy)
            noise = np.random.normal(0, self.perturbation_scale, size=strategy.shape)
            perturbed_strategy = strategy + noise
            # Ensure non-negativity and re-normalize
            perturbed_strategy = np.clip(perturbed_strategy, 0, None)
            if perturbed_strategy.sum() > 0:
                perturbed_strategy /= perturbed_strategy.sum()
            else:
                perturbed_strategy = strategy
            perturbed_profile[player] = perturbed_strategy.tolist()
        stable = NashEquilibriumSolver().is_equilibrium(perturbed_profile, game)
        logger.debug(f"Perturbed equilibrium stability: {stable}")
        return stable


class DynamicEquilibriumManager:
    """
    Manages equilibria in dynamic, multi-stage games by recalculating
    and updating equilibria as the game state evolves.

    Attributes:
        solver (EquilibriumSolver): The equilibrium solver to use.
        current_equilibrium (Equilibrium): The current equilibrium state.
    """

    def __init__(self, solver: EquilibriumSolver):
        self.solver = solver
        self.current_equilibrium = None

    def update_equilibrium(self, game):
        """
        Recalculates the equilibrium for the current game state.

        :param game: An instance of Game.
        :return: The updated Equilibrium.
        """
        self.current_equilibrium = self.solver.compute_equilibrium(game)
        logger.debug(f"Dynamic equilibrium updated: {self.current_equilibrium}")
        return self.current_equilibrium

    def get_equilibrium(self):
        """
        Returns the current equilibrium.
        """
        return self.current_equilibrium


class ApproximationSolver(EquilibriumSolver):
    """
    Provides approximate equilibrium solutions for games where exact computation is NP-hard.
    This implementation uses heuristics to generate an approximate strategy profile.
    """

    def compute_equilibrium(self, game):
        strategy_profile = {player: np.random.rand() for player in game.players}
        eq = Equilibrium(strategy_profile, stability_metric=0.9)  # Slightly lower stability
        logger.debug(f"Approximate equilibrium computed: {eq}")
        return eq

    def is_equilibrium(self, strategy_profile, game):
        deviations = game.get_deviations(strategy_profile)
        for player in game.players:
            # Allow for a 10% tolerance in deviation payoffs
            if deviations[player] > game.expected_payoff(player, strategy_profile) * 1.1:
                return False
        return True


class GraphicalEquilibrium(EquilibriumSolver):
    """
    Computes equilibria for network-based games where players are represented as nodes.
    For demonstration, returns a uniform strategy profile.
    """

    def compute_equilibrium(self, game):
        strategy_profile = {player: (np.ones(3) / 3).tolist() for player in game.players}
        eq = Equilibrium(strategy_profile, stability_metric=1.0)
        logger.debug(f"Graphical equilibrium computed: {eq}")
        return eq

    def is_equilibrium(self, strategy_profile, game):
        deviations = game.get_deviations(strategy_profile)
        for player in game.players:
            if deviations[player] > game.expected_payoff(player, strategy_profile):
                return False
        return True


# =============================================================================
# Example Usage for Testing and Demonstration
# =============================================================================
if __name__ == "__main__":
    # Create a dummy two-player game with a sample payoff matrix.
    payoff_matrix = [[1, -1, 0],
                     [0, 1, -1]]
    players = ["Player1", "Player2"]
    game = Game(payoff_matrix, players)

    # Compute a Nash Equilibrium.
    nash_solver = NashEquilibriumSolver()
    equilibrium_nash = nash_solver.compute_equilibrium(game)
    print("Nash Equilibrium:", equilibrium_nash)

    # Test the stability of the computed equilibrium under perturbation.
    perturbed_test = PerturbedEquilibrium(equilibrium_nash)
    stability = perturbed_test.test_stability(game)
    print("Perturbed Stability:", stability)