import unittest
from scanner.static_analysis import StaticAnalyzer


class TestStaticAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = StaticAnalyzer()

    def test_analyze_source_code_no_vulnerabilities(self):
        source_code = """
        <html>
            <head></head>
            <body>
                <h1>Hello, World!</h1>
            </body>
        </html>
        """

        self.analyzer.analyze_source_code(source_code)
        vulnerabilities = self.analyzer.get_vulnerabilities()

        self.assertEqual(len(vulnerabilities), 0)

    def test_analyze_source_code_with_vulnerabilities(self):
        source_code = """
        <html>
            <head></head>
            <body>
                <input type="text" value="test">
                <script>
                    var password = 'test';
                    // Example of potential XSS vulnerability
                    document.write(password);
                </script>
            </body>
        </html>
        """

        self.analyzer.analyze_source_code(source_code)
        vulnerabilities = self.analyzer.get_vulnerabilities()

        self.assertEqual(len(vulnerabilities), 1)
        self.assertIn("Potential XSS vulnerability found", vulnerabilities)


if __name__ == '__main__':
    unittest.main()
