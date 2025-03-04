"""
This module provides Base Classes for *all* **game theory** mechanics; such as *players* or *strategies*.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any
from uuid import uuid4, UUID

from pydantic import UUID4

from gameforged.control_tower import LOG as log


class GameTheoryMechanic(ABC):
    """
    Identifying base class for a mechanics of game theory (e.g. *players* or *strategies*)
    """
    mechanic_name = 'game theory'
    @abstractmethod
    def __init__(self):
        self._uid = uuid4()
        self._label: str = ''

    @property
    def identifier(self):
        return self._uid

    def set_id(self, uid: str | UUID | UUID4 | None):
        """
        Set the unique identifier for the instance.

        :param uid: string or UUID
        :return: nothing
        """
        if isinstance(uid, str):
            self._uid = UUID(uid)
            log.success(f"{self.mechanic_name.capitalize()} ID set to: {self._uid}")
        elif isinstance(uid, UUID):
            self._uid = uid
            log.success(f"{self.mechanic_name.capitalize()} ID set to: {self._uid}")
        elif uid is None:
            log.warning("No ID provided. Generating a new one.")
            self._uid = uuid4()
            log.success(f"{self.mechanic_name.capitalize()} ID set to: {self._uid}")
        else:  # TODO: Catch & Handle invalid UID type issue
            log.error(f"Invalid UID type: {type(uid)}")

    @property
    def name(self) -> str:
        return self._label

    def set_name(self, label: str):
        """
        Set the name of the strategy.
        :param label:
        :return: nothing
        """
        self._label = label
        log.success(f"{self.mechanic_name.capitalize()} name set to: {self._label}")

class BaseAgent(GameTheoryMechanic, ABC):
    """
    Abstract base class for decision-makers in a game.
    """
    mechanic_name = 'agents'
    mechanic_desc = 'decision-makers in a game'

    @abstractmethod
    def __init__(self):
        super().__init__()
        self._is_simulated = False

class BaseGame(GameTheoryMechanic, ABC):
    """
    An *abstract base class* for a **game**; a Structured interaction involving players making strategic decisions.
    """

    mechanic_name = 'games'
    mechanic_desc = 'a structured interaction involving players making strategic decisions.'

    @abstractmethod
    def __init__(self, name, uid, rulebook):
        """
        Initialize the 'game' mechanics.
        """
        super().__init__()
        self._game_id = uid
        self._label = name
        self.rulebook = rulebook
        self._players = []
        self.turn_number = 0
        self.state = {}
        self.history = []
        self.started = False
        self.ended = False

    @property
    def current_turn(self):
        if self.history:
            return self.history[-1]
        return None

    @property
    def active_players(self):
        return [p for p in self.players if p.status == 'active']

    def start_game(self):
        self.started = True
        self.turn_number = 1
        self._init_game_state()

    def end_game(self):
        self.ended = True

    def advance_turn(self):
        self.turn_number += 1

    def add_player(self, player):
        self.players.append(player)

    def log_action(self, player_id, action, result):
        self.history.append(
            {
            'turn': self.turn_number,
            'player': player_id,
            'action': action,
            'result': result
            }
        )

    @abstractmethod
    def get_winner(self):
        pass  # Game-specific

    def _init_game_state(self):
        self.state = {}  # Can be overridden by subclasses

    @property
    def players(self):
        return self._players


class BasePayoff(GameTheoryMechanic, ABC):
    """
    Quantification of outcomes based on players' actions.
    """
    mechanic_name = 'payoffs'
    mechanic_desc = 'quantification of outcomes based on players\' actions'

    @abstractmethod
    def __init__(self):
        super().__init__()


class BaseStrategy(GameTheoryMechanic, ABC):  # TODO: document strategy base class
    """
    Abstract base class for strategies used by players in a game.
    """

    mechanic_name = 'strategies'
    mechanic_desc = ''

    @abstractmethod
    def __init__(self, name: str | None = 'new strategy', uid: str | UUID | None = None):
        """

        :param name:
        :param uid:
        """
        super().__init__()
        self._label: str = 'new strategy'
        self._uid = str(uuid4())
        self._stype = 'unknown'
        if uid:
            self.set_id(uid)

        if name:
            self.set_name(name)
        else:
            self.set_name('new strategy')

        log.debug(f"Strategy initialized: '{self._label}'  ({self._uid})")




    @property
    def strategy_id(self) -> UUID | str:
        return self._uid



class BaseAction(GameTheoryMechanic, ABC):  # TODO: add hooks to this class
    """

    """

    mechanic_name = 'actions'

    @abstractmethod
    def __init__(self):
        super().__init__()




class BaseInformation(GameTheoryMechanic, ABC):  # TODO: add hooks to this class
    """
    TODO: Document BaseInformation class
    """
    @abstractmethod
    def __init__(self):
        super().__init__()
        self.global_information: Dict[str, Dict[str, Any]] = {}
        self.player_information: Dict[str, Dict[str, Dict[str, Any]]] = {}

    @abstractmethod
    def get_information(self):
        pass

    def get_all_information(self):
        return {
            "global": self.global_information,
            "players": self.player_information
        }

class BaseTurn(GameTheoryMechanic, ABC):  # TODO: add hooks to this class
    """
    TODO: Document BaseTurn class
    """

    mechanic_name = 'turns'
    mechanic_desc = ''  # TODO: Add description

    @abstractmethod
    def __init__(self):
        super().__init__()


# TODO: Add a hook/extension implementation for custom mechanics abstract bases