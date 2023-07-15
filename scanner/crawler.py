import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self):
        self.visited_urls = set()
        self.target_domain = None
        self.source_code_paths = []

    def crawl(self, target_url, max_depth):
        self.target_domain = urlparse(target_url).netloc
        self._crawl_recursive(target_url, 1, max_depth)
        return self.visited_urls

    def _crawl_recursive(self, url, current_depth, max_depth):
        if current_depth > max_depth:
            return

        if url in self.visited_urls:
            return

        self.visited_urls.add(url)

        try:
            response = requests.get(url)
        except requests.exceptions.RequestException:
            return

        if response.status_code != 200:
            return

        self._process_response(url, response)

        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href")
            if href:
                absolute_url = urljoin(url, href)
                if self._is_valid_url(absolute_url):
                    self._crawl_recursive(
                        absolute_url, current_depth + 1, max_depth)

    def _is_valid_url(self, url):
        parsed_url = urlparse(url)
        if parsed_url.scheme not in ["http", "https"]:
            return False
        if parsed_url.netloc != self.target_domain:
            return False
        if "#" in parsed_url.path:
            return False
        return True

    def _process_response(self, url, response):
        # Additional processing logic for the response (e.g., parsing source code, extracting relevant information)
        if response.headers.get("content-type") == "text/html":
            self.source_code_paths.append(url)

    def get_source_code_paths(self):
        return self.source_code_paths
