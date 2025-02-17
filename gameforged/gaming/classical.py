from gameforged.__bases__ import BaseAgent, BaseGame

class ClassicalPlayer(BaseAgent):
    def __init__(self):
        pass

class ClassicalGame(BaseGame):
    def __init__(self):
        pass

    def __repr__(self):
        return f"ClassicalGame()"  # TODO: String rep