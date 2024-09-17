# analyzer/reporter.py

from colorama import Fore, Style

class Reporter:
    def __init__(self, issues):
        self.issues = issues

    def generate_report(self):
        if not self.issues:
            print(Fore.GREEN + "No issues found. Your code is clean!")
            return

        for issue in self.issues:
            print(Fore.RED + f"Issue {issue['rule_id']} ({issue['severity']} Severity): {issue['message']}")
            print(Fore.YELLOW + f"File: {issue['file']}:{issue['line']}:{issue['column']}")
            print(Style.RESET_ALL + "-" * 50)
