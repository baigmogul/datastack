import json
from rule import Rule


class RulesEngine:

    def __init__(self, rules_config):
        if not rules_config:
            raise Exception("Config file not provided")
        self.rules = []
        self.rules_config = rules_config
        self.load_rules()

    def load_rules(self):
        for rule in self.rules_config["rules"]:
            # create a rule object and add it to the list of rules also check if the constraints are empty
            if rule["constraints"]:
                self.rules.append(
                    Rule((rule["cell"][0], rule["cell"][1]), 
                    rule["constraints"]["left"], rule["constraints"]["right"], 
                    rule["constraints"]["up"], rule["constraints"]["down"], 
                    rule["constraints"]["operator"])
                    )
            else:
                self.rules.append(Rule((rule["cell"][0], rule["cell"][1])))
    def get_rules(self):
        return self.rules

    def add_rule(self, op, cell, left=False, right=False, up=False, down=False):
        self.rules.append(Rule(cell, left, right, up, down, op))