# analyzer/analyzer.py

import ast
import os
from .rules import RULES

class Analyzer:
    def __init__(self, path):
        self.path = path
        self.issues = []

    def analyze_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            tree = ast.parse(file.read(), filename=file_path)

        for node in ast.walk(tree):
            for rule_class in RULES:
                rule = rule_class()
                if rule.check(node):
                    issue = {
                        'file': file_path,
                        'line': node.lineno,
                        'column': node.col_offset,
                        'rule_id': rule.id,
                        'message': rule.short_description,
                        'severity': rule.severity,
                    }
                    self.issues.append(issue)

    def run(self):
        if os.path.isfile(self.path) and self.path.endswith('.py'):
            self.analyze_file(self.path)
        else:
            for root, _, files in os.walk(self.path):
                for file in files:
                    if file.endswith('.py'):
                        file_path = os.path.join(root, file)
                        self.analyze_file(file_path)

    def get_issues(self):
        return self.issues
