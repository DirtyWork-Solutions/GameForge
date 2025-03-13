"""This module defines a framework for modeling and injecting human cognitive biases and behavioral tendencies into
player decision-making processes. It is designed to be a flexible, optional layer that can be attached to player
strategies or AI models to simulate irrationality, psychological tendencies, or bounded rationality in games.

The purpose is to enhance realism in both human-mimicking AI players and in player modeling for research or experimental
simulations.

Concept: This acts like a middleware or influence layer between "rational decision-making" and "actual decisions taken".

**Core Biases Supported** *(to be expanded)*:

- Loss Aversion
- Risk Aversion
- Anchoring Bias
- Recency Bias
- Overconfidence Bias
- Sunk Cost Fallacy
- Framing Effects
- Social Conformity

This module does not store player state — it purely "filters" decision inputs/outputs.
"""

from typing import Optional, Union, List, Dict, Any
from enum import Enum
import random
from gameforged.control_tower import Controller

logger = Controller().logger

class BiasType(str, Enum):  # TODO: Add hook for custom biases
    """Enumeration of supported cognitive biases."""
    LOSS_AVERSION = "loss_aversion"
    RISK_AVERSION = "risk_aversion"
    ANCHORING = "anchoring"
    RECENCY = "recency"
    OVERCONFIDENCE = "overconfidence"
    SUNK_COST = "sunk_cost"
    FRAMING_EFFECT = "framing"
    SOCIAL_CONFORMITY = "social_conformity"


class BiasProfile:
    """
    Each player (if desired) can have a BiasProfile, which defines the strength and presence
    of various biases. This is attached to a player strategy or decision engine.

    Biases range from 0 (no bias) to 1 (strong bias). Profiles are optional and customizable per player.
    """
    def __init__(self, player_id: str, bias_strengths: Optional[Dict[BiasType, float]] = None):
        self.player_id = player_id
        self.bias_strengths = bias_strengths or {
            bias: 0.0 for bias in BiasType
        }

    def set_bias(self, bias: BiasType, strength: float):
        """Set the strength of a specific bias."""
        self.bias_strengths[bias] = max(0.0, min(1.0, strength))

    def get_bias_strength(self, bias: BiasType) -> float:
        """Retrieve the current strength of a specific bias."""
        return self.bias_strengths.get(bias, 0.0)


class BiasInfluencer:
    """
    This class acts as the core "bias processor" — it takes rational decisions or evaluations and modifies
    them based on the player's bias profile.

    It does not decide actions directly — it distorts or nudges decisions already made (or expected payoffs) to reflect biases.
    """
    def __init__(self, player_id: str, bias_profile: BiasProfile):
        self.player_id = player_id
        self.bias_profile = bias_profile

    def apply_bias_to_payoff(self, original_payoff: float, reference_point: Optional[float] = None) -> float:
        """
        Distort perceived payoff based on biases like loss aversion and framing effects.

        :param original_payoff: The rationally computed payoff.
        :param reference_point: Optional — a previous known state for anchoring or framing.
        :return: Biased, psychologically adjusted payoff.
        """
        adjusted_payoff = original_payoff

        # Loss Aversion — Losses feel more painful than equal gains feel good
        if adjusted_payoff < 0 and self.bias_profile.get_bias_strength(BiasType.LOSS_AVERSION) > 0:
            multiplier = 1 + (2 * self.bias_profile.get_bias_strength(BiasType.LOSS_AVERSION))
            adjusted_payoff *= multiplier

        # Framing Effect — The way the outcome is framed (gain/loss) affects perception
        if reference_point is not None:
            framed_as_gain = (original_payoff >= reference_point)
            if not framed_as_gain and self.bias_profile.get_bias_strength(BiasType.FRAMING_EFFECT) > 0:
                adjusted_payoff *= (1 + self.bias_profile.get_bias_strength(BiasType.FRAMING_EFFECT))

        return adjusted_payoff

    def apply_bias_to_risk_evaluation(self, riskiness: float) -> float:
        """
        Modify risk evaluation based on risk aversion or overconfidence biases.

        :param riskiness: Base rational risk level (0 = safe, 1 = high risk).
        :return: Biased perceived risk.
        """
        adjusted_risk = riskiness

        # Risk Aversion — Overestimate dangers of higher risk actions
        if self.bias_profile.get_bias_strength(BiasType.RISK_AVERSION) > 0:
            adjusted_risk *= (1 + self.bias_profile.get_bias_strength(BiasType.RISK_AVERSION))

        # Overconfidence — Underestimate all risk levels
        if self.bias_profile.get_bias_strength(BiasType.OVERCONFIDENCE) > 0:
            adjustment = 1 - (0.5 * self.bias_profile.get_bias_strength(BiasType.OVERCONFIDENCE))
            adjusted_risk *= adjustment

        return max(0, min(1, adjusted_risk))

    def apply_bias_to_action_selection(self, available_actions: List[str], suggested_action: str) -> str:
        """
        Potentially override or modify the player's selected action based on conformity, recency, etc.

        :param available_actions: All valid actions.
        :param suggested_action: Rationally suggested action.
        :return: Biased action selection.
        """
        biased_action = suggested_action

        # Recency Bias — Overweight the last action performed
        if self.bias_profile.get_bias_strength(BiasType.RECENCY) > 0:
            if len(available_actions) > 1 and random.random() < self.bias_profile.get_bias_strength(BiasType.RECENCY):
                biased_action = available_actions[-1]

        # Social Conformity — Favor actions others are taking (external signal needed from game)
        # Placeholder - could eventually query external 'most common action'
        # if self.bias_profile.get_bias_strength(BiasType.SOCIAL_CONFORMITY) > 0:
        # biased_action = self.get_most_common_action(available_actions)

        return biased_action

    # TODO: needs input from game state -
    # def get_most_common_action(self, available_actions: List[str]) -> str:
    # return random.choice(available_actions)