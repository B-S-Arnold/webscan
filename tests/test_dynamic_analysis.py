import unittest
from scanner.dynamic_analysis import DynamicAnalyzer


class TestDynamicAnalyzer(unittest.TestCase):
    def test_analyze_finds_vulnerabilities(self):
        # Create an instance of DynamicAnalyzer
        analyzer = DynamicAnalyzer()

        # Simulate a list of source code paths
        source_code_paths = ["http://example.com/path1",
                             "http://example.com/path2"]

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

        analyzer._fetch_source_code = mock_get

        # Run the analysis
        analyzer.analyze("http://example.com", source_code_paths)

        # Get the detected vulnerabilities
        vulnerabilities = analyzer.get_vulnerabilities()

        # Check if the expected vulnerability is found
        self.assertIn("Hardcoded password found", vulnerabilities)


if __name__ == '__main__':
    unittest.main()
