class RuleEngine:
    def __init__(self):
        self.rules = {}
        self.constraints = {}

    def register_rule(self, rule):
        self.rules[rule.id] = rule

    def register_constraint(self, constraint):
        self.constraints[constraint.id] = constraint

    def validate_action(self, action, context):
        violations = []
        for rule in self.rules.values():
            if not rule.condition(action, context):
                violations.append(rule)
        return violations

    def apply_constraints(self, action, context):
        results = {}
        for constraint in self.constraints.values():
            results[constraint.id] = constraint.condition(action, context) if constraint.condition else True
        return results
