import random

class FramingHeuristics:
    @staticmethod
    def round_to_nearest_five(time: float) -> float:
        return round(time / 5) * 5 # People like 9:35, 9:40, etc.

    @staticmethod
    def social_norm_bias(base_time: float, preferred_time: float) -> float:  # TODO: Import
        # Players bias towards the "socially typical" time if within 3 minutes
        if abs(base_time - preferred_time) <= 3:
            return preferred_time
        return base_time

class LossAversion:
    @staticmethod
    def penalize_late_arrival(arrival_time: float, latest_time: float, loss_penalty: float = 2.0) -> float:
        if arrival_time > latest_time:
            return loss_penalty * (arrival_time - latest_time)
        return 0