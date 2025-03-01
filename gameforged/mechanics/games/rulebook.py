from gameforged.rules.engine import RuleEngine


class Rulebook:
    def __init__(self):
        self.engine = RuleEngine()
        self.history = []

    def initialize(self, rules, constraints):
        for rule in rules:
            self.engine.register_rule(rule)
        for constraint in constraints:
            self.engine.register_constraint(constraint)

    def evaluate_action(self, action, context):
        violations = self.engine.validate_action(action, context)
        constraints = self.engine.apply_constraints(action, context)
        self.history.append((action, context, violations, constraints))
        return violations, constraints

    def log_mutation(self, mutation_event):
        self.history.append(('MUTATION', mutation_event))

