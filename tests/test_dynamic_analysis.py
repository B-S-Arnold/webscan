import unittest
from scanner.dynamic_analysis import DynamicAnalyzer
from unittest.mock import patch


class TestDynamicAnalyzer(unittest.TestCase):
    def test_analyze_finds_vulnerabilities(self):
        # Simulate a source code with a hardcoded vulnerability
        source_code = """
        <html>
            <head></head>
            <body>
                <input type="password" value="secret">
            </body>
        </html>
        """

        # Mock the requests.get method to return the simulated source code
        class MockResponse:
            def __init__(self, text):
                self.text = text

        def mock_get(url):
            return MockResponse(source_code)

        # Use the patch decorator to temporarily replace the _fetch_source_code method
        with patch("scanner.dynamic_analysis.DynamicAnalyzer._fetch_source_code", side_effect=mock_get):
            # Create an instance of DynamicAnalyzer
            analyzer = DynamicAnalyzer()

            # Simulate a list of source code paths
            source_code_paths = [
                "http://example.com/path1", "http://example.com/path2"]

            # Run the analysis
            analyzer.analyze("http://example.com", source_code_paths)

            # Get the detected vulnerabilities
            vulnerabilities = analyzer.get_vulnerabilities()

            # Check if the expected vulnerability is found
            expected_vulnerability = "Hardcoded password found"
            self.assertIn(expected_vulnerability, vulnerabilities)


if __name__ == '__main__':
    unittest.main()
