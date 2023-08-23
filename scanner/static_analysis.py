import re

class StaticAnalyzer:
    def __init__(self):
        self.vulnerabilities = []

    def analyze_source_code(self, source_code):
        vulnerabilities = self._find_vulnerabilities(source_code)
        self.vulnerabilities.extend(vulnerabilities)

    def _find_vulnerabilities(self, source_code):
        # Example: Finding SQL injection vulnerabilities using regular expressions
        sql_injection_pattern = re.compile(
            r"SELECT \* FROM users WHERE username='(.+)' AND password='(.+)'")
        vulnerabilities = []
        if sql_injection_pattern.search(source_code):
            vulnerabilities.append(
                "Potential SQL injection vulnerability found")
        return vulnerabilities

    def get_vulnerabilities(self):
        return self.vulnerabilities
