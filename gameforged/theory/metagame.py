from collections import defaultdict
from typing import Optional


class ArrivalHistory:
    def __init__(self):
        self.history = defaultdict(list)

    def record_arrival(self, player: str, arrival_time: float):
        self.history[player].append(arrival_time)

    def get_average_arrival(self, player: str) -> Optional[float]:
        if not self.history[player]:
            return None
        return sum(self.history[player]) / len(self.history[player])

class AdaptiveStrategy:
    @staticmethod
    def shift_toward_opponent(arrival_time: float, opponent_average: Optional[float]) -> float:
        if opponent_average is None:
            return arrival_time # No data yet
        return (arrival_time + opponent_average) / 2
