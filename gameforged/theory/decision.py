import random

class FramingHeuristics:
    """
    A collection of static methods for applying framing heuristics to decision-making processes.
    These heuristics adjust times to more socially typical values.
    """
    @staticmethod
    def round_to_nearest_five(time: float) -> float:
        """
        Round the given time to the nearest multiple of five.

        :param time: The time to be rounded.
        :return: The time rounded to the nearest multiple of five.
        """
        return round(time / 5) * 5 # People like 9:35, 9:40, etc.

    @staticmethod
    def social_norm_bias(base_time: float, preferred_time: float) -> float:  # TODO: Import
        """
        Bias the base time towards a socially typical time if within a 3-minute window.

        :param base_time: The original time.
        :param preferred_time: The socially typical time.
        :return: The biased time if within 3 minutes of the preferred time, otherwise the base time.
        """
        # Players bias towards the "socially typical" time if within 3 minutes
        if abs(base_time - preferred_time) <= 3:
            return preferred_time
        return base_time

class LossAversion:
    """
    A collection of static methods for applying loss aversion principles to decision-making processes.
    These methods penalize late arrivals based on a specified penalty factor.
    """
    @staticmethod
    def penalize_late_arrival(arrival_time: float, latest_time: float, loss_penalty: float = 2.0) -> float:
        """
        Calculate a penalty for arriving later than the latest acceptable time.

        :param arrival_time: The actual arrival time.
        :param latest_time: The latest acceptable arrival time.
        :param loss_penalty: The penalty factor for late arrival.

        :return: The calculated penalty if arrival is late, otherwise 0.
        """
        #
        if arrival_time > latest_time:
            return loss_penalty * (arrival_time - latest_time)
        return 0