# TODO: document rule module
from uuid import uuid4


# TODO: create rule module

class Rule:
    def __init__(self, rule_id, description, condition, scope, priority, mutable=True):
        # Presets
        self.id = rule_id if rule_id is not None else uuid4()
        self.description: str = description if description is not None else 'unknown rule'
        self.condition = condition # Callable that evaluates the rule
        self.scope: str = scope.lower() # Global, Player, Phase, etc.
        self.priority = priority
        self.mutable: bool = mutable