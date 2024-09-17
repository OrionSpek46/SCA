# analyzer/rules.py

import ast

class BaseRule:
    id = 'SCP000'
    short_description = 'Base Rule'
    description = 'This is the base rule class.'
    severity = 'LOW'

    def check(self, node):
        pass

class HardCodedPasswordRule(BaseRule):
    id = 'SCP001'
    short_description = 'Hard-coded password detected.'
    description = 'Avoid using hard-coded passwords in code.'
    severity = 'HIGH'

    def check(self, node):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and 'password' in target.id.lower():
                    if isinstance(node.value, ast.Str):
                        return True
        return False

# Add more rules as needed

# List of all rule classes
RULES = [HardCodedPasswordRule()]
