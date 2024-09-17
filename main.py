# main.py

import argparse
from analyzer.analyzer import Analyzer
from analyzer.reporter import Reporter

def main():
    parser = argparse.ArgumentParser(description='Secure Coding Practices Analyzer')
    parser.add_argument('path', help='Path to the file or directory to analyze')
    args = parser.parse_args()

    analyzer = Analyzer(args.path)
    analyzer.run()

    reporter = Reporter(analyzer.get_issues())
    reporter.generate_report()

if __name__ == '__main__':
    main()
