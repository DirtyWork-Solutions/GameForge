class Rule:
    def __init__(self, id, description, condition, scope, priority, mutable=True):
        self.id = id
        self.description = description
        self.condition = condition # Callable that evaluates the rule
        self.scope = scope # Global, Player, Phase, etc.
        self.priority = priority
        self.mutable = mutable