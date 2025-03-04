from pydantic import BaseModel
from typing import Optional

class TimingDecision(BaseModel):
    player_id: str
    arrival_time: float # Time in minutes since the start of the window (e.g., 0 = 9:30, 15 = 9:45)

class TimingOutcome(BaseModel):
    player_id: str
    wait_time: float # How long they waited for the other player
    departure_time: float # When the cab actually departed

class TimingGame(BaseModel):
    players: list[str]
    time_window: tuple[float, float] # Start and end in minutes (e.g., (0, 15) for 9:30-9:45)

    def validate_arrival(self, arrivals: dict[str, float]) -> Optional[TimingOutcome]:
        if len(arrivals) < 2:
            return None # Both players need to arrive

        earliest = max(arrivals.values())
        for player, arrival in arrivals.items():
            yield TimingOutcome(
                player_id=player,
                wait_time=earliest - arrival,
                departure_time=earliest
            )

    def payoff(self, wait_time: float, departure_time: float) -> float:
        # Example: Payoff favors earlier departure, penalizes waiting
        return -wait_time - (departure_time / 60.0) # Prefer to leave early, dislike waiting


if __name__ == '__main__':
    game = TimingGame(players=["A", "B"], time_window=(0, 15))

    arrivals = {"A": 3.5, "B": 4.0}  # A arrives at 9:33.5, B at 9:34
    outcomes = list(game.validate_arrival(arrivals))

    for outcome in outcomes:
        print(f"Player {outcome.player_id} waits {outcome.wait_time:.1f} minutes")
        print(f"Cab departs at 9:{30 + outcome.departure_time:.1f}")
