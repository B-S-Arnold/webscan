class ReportGenerator:
    def __init__(self):
        self.vulnerabilities = []

    def add_vulnerability(self, vulnerability):
        self.vulnerabilities.append(vulnerability)

    def generate_report(self):
        report = "Vulnerability Report:\n\n"
        if self.vulnerabilities:
            for index, vulnerability in enumerate(self.vulnerabilities, start=1):
                report += f"{index}. {vulnerability}\n"
        else:
            report += "No vulnerabilities found.\n"
        return report
