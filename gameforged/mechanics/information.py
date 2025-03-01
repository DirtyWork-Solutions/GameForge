"""
This module defines how information is shared, hidden, or distorted 
among players in a game.


**Key Components:**

- InformationSet *(Abstract Base Class)*: Defines the basic interface for information access.
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
from gameforged.control_tower import LOG as log

from typing import Dict, Any, Optional, Callable, List, Union

class InformationManager:
    """
    Advanced Information Manager for GameForge.


    **Supports:**

    - Public and player-specific information.
    - Multi-layer *(namespaced) information handling (military, economic, etc.).
    - Per-layer visibility, filtering, and logging.
    - Meta-information tracking (source, authenticity, modification history).
    - Optional access policies (who can access what and when).
    """

    def __init__(self):
        self.global_information: Dict[str, Dict[str, Any]] = {}
        self.player_information: Dict[str, Dict[str, Dict[str, Any]]] = {}

        # Optional Components
        self.visibility_rules: Dict[str, List[Callable[[str, str, Dict[str, Any]], bool]]] = {}
        self.filters: Dict[str, List[Callable[[Dict[str, Any]], Dict[str, Any]]]] = {}
        self.audit_log: List[Dict[str, Any]] = []
        self.access_policies: Dict[str, Dict[str, Dict[str, bool]]] = {}

    # ===== Core Operations =====

    def initialize(self, game_state: Optional[Dict[str, Any]] = None):
        """
        Initialize the information manager, optionally with the initial game state.
        :param game_state:
        :return: nothing
        """
        if game_state:
            self.global_information = game_state.get("public", {})
            self.player_information = game_state.get("private", {})

    def update(self, event: Dict[str, Any]):
        self._log_audit("event", event)
        for layer, updates in event.get('public_updates', {}).items():
            self.global_information.setdefault(layer, {}).update(updates)

        for player_id, player_data in event.get('player_updates', {}).items():
            for layer, updates in player_data.items():
                self.player_information.setdefault(player_id, {}).setdefault(layer, {}).update(updates)

    # ===== Information Retrieval =====

    def get_public_information(self, layer: str) -> Dict[str, Any]:
        info = self.global_information.get(layer, {}).copy()
        return self._apply_filters(layer, info)

    def get_player_information(self, player_id: str, layer: str) -> Dict[str, Any]:
        base_info = self.player_information.get(player_id, {}).get(layer, {}).copy()
        return self._apply_filters(layer, base_info)

    def reveal_information(self, player_id: str, layer: str, key: str, value: Any, source: str = None, authenticity: str = None):
        meta_value = self._wrap_meta_information(value, source, authenticity)
        self._log_audit("reveal", {"player": player_id, "layer": layer, "key": key, "value": meta_value})
        self.player_information.setdefault(player_id, {}).setdefault(layer, {})[key] = meta_value

    def conceal_information(self, player_id: str, layer: str, key: str):
        self._log_audit("conceal", {"player": player_id, "layer": layer, "key": key})
        self.player_information.get(player_id, {}).get(layer, {}).pop(key, None)

    # ===== Meta Information Handling =====

    def _wrap_meta_information(self, value: Any, source: Optional[str], authenticity: Optional[str]) -> Dict[str, Any]:
        return {
            "value": value,
            "source": source or "system",
            "authenticity": authenticity or "unknown",
            "modification_history": []
        }

    # ===== Optional Visibility Rules =====

    def add_visibility_rule(self, layer: str, rule: Callable[[str, str, Dict[str, Any]], bool]):
        self.visibility_rules.setdefault(layer, []).append(rule)

    def _is_visible(self, player_id: str, layer: str, key: str, context: Dict[str, Any]) -> bool:
        for rule in self.visibility_rules.get(layer, []):
            if not rule(player_id, key, context):
                return False
        return True

    # ===== Optional Filters =====

    def add_filter(self, layer: str, filter_func: Callable[[Dict[str, Any]], Dict[str, Any]]):
        self.filters.setdefault(layer, []).append(filter_func)

    def _apply_filters(self, layer: str, info: Dict[str, Any]) -> Dict[str, Any]:
        for filter_func in self.filters.get(layer, []):
            info = filter_func(info)
        return info

    # ===== Optional Audit Log =====

    def _log_audit(self, action: str, data: Dict[str, Any]):
        self.audit_log.append({"action": action, "data": data})

    def get_audit_log(self) -> List[Dict[str, Any]]:
        return self.audit_log

    # ===== Optional Dynamic Access Policies =====

    def set_access_policy(self, player_id: str, layer: str, key: str, can_access: bool):
        self.access_policies.setdefault(player_id, {}).setdefault(layer, {})[key] = can_access

    def can_access(self, player_id: str, layer: str, key: str) -> bool:
        return self.access_policies.get(player_id, {}).get(layer, {}).get(key, True)

    # ===== Combined Layered Visibility Check =====

    def get_filtered_player_information(self, player_id: str, layer: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        context = context or {}
        player_info = self.get_player_information(player_id, layer)

        visible_info = {}
        for key, meta in player_info.items():
            if self.can_access(player_id, layer, key) and self._is_visible(player_id, layer, key, context):
                visible_info[key] = meta
        return visible_info



# ----------------------------------------------------

class PerfectInformation(BaseInformation):  # TODO: Create PerfectInformation class
    pass


class ImperfectInformation(BaseInformation):  # TODO: Create ImperfectInformation class
    pass


class AsymmetricInformation(BaseInformation):  # TODO: Create AsymmetricInformation class
    pass


class MisinformationMechanic(BaseInformation):  # TODO: Create Misinformation class
    pass