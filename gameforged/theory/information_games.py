
class PublicClock:
    @staticmethod
    def broadcast_arrival(arrival_time: float) -> str:
        return f"Public clock: Player has arrived at 9:{30 + arrival_time:.1f}"