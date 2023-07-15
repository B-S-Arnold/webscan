import unittest
from crawler import Crawler


class TestCrawler(unittest.TestCase):
    def setUp(self):
        self.crawler = Crawler()

    def test_crawl(self):
        target_url = "https://example.com"
        max_depth = 2

        visited_urls = self.crawler.crawl(target_url, max_depth)

        # Assuming there are 4 unique URLs within 2 levels
        self.assertEqual(len(visited_urls), 4)

        # Additional assertions to verify specific URLs were visited or not
        self.assertIn(target_url, visited_urls)
        self.assertIn("https://example.com/page1", visited_urls)
        self.assertIn("https://example.com/page2", visited_urls)
        self.assertIn("https://example.com/page3", visited_urls)

    def test_get_source_code_paths(self):
        self.crawler.source_code_paths = [
            "https://example.com/source1",
            "https://example.com/source2",
            "https://example.com/source3"
        ]

        source_code_paths = self.crawler.get_source_code_paths()

        self.assertEqual(len(source_code_paths), 3)
        self.assertIn("https://example.com/source1", source_code_paths)
        self.assertIn("https://example.com/source2", source_code_paths)
        self.assertIn("https://example.com/source3", source_code_paths)


if __name__ == "__main__":
    unittest.main()
