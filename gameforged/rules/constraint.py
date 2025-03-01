# TODO: Create and implement abstract base class(es) for constraints and import them
# TODO: Document constraints module


class Constraint:  
    def __init__(self, id, type, value, scope, condition=None):
        self.id = id
        self.type = type # Numerical, Relational, Progression
        self.value = value
        self.scope = scope
        self.condition = condition # Optional callable for dynamic constraints