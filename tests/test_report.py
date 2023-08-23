import unittest
from scanner.report import ReportGenerator


class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        self.report_generator = ReportGenerator()

    def test_generate_report_no_vulnerabilities(self):
        report = self.report_generator.generate_report()
        expected_report = "Vulnerability Report:\n\nNo vulnerabilities found.\n"
        self.assertEqual(report, expected_report)

    def test_generate_report_with_vulnerabilities(self):
        self.report_generator.add_vulnerability(
            "Cross-site Scripting (XSS) in login form")
        self.report_generator.add_vulnerability(
            "Insecure Direct Object References (IDOR)")

        report = self.report_generator.generate_report()
        expected_report = "Vulnerability Report:\n\n1. Cross-site Scripting (XSS) in login form\n2. Insecure Direct Object References (IDOR)\n"
        self.assertEqual(report, expected_report)


if __name__ == '__main__':
    unittest.main()
