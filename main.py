from scanner.crawler import Crawler
from scanner.http import HttpClient
from scanner.vulnerability import VulnerabilityScanner
from scanner.static_analysis import StaticAnalyzer
from scanner.dynamic_analysis import DynamicAnalyzer
from scanner.report import ReportGenerator


def main():
    # Configure settings and target website
    target_url = "https://example.com"
    max_depth = 10  # Maximum depth for crawling
    
    # Initialize scanner components
    crawler = Crawler()
    http_client = HttpClient()
    vulnerability_scanner = VulnerabilityScanner()
    static_analyzer = StaticAnalyzer()
    dynamic_analyzer = DynamicAnalyzer()
    report_generator = ReportGenerator()
    
    # Step 1: Crawl the target website
    
    crawled_urls = crawler.crawl(target_url, max_depth)

    # Step 2: Perform static analysis on source code
    
    source_code_paths = crawler.get_source_code_paths()
    static_analysis_results = static_analyzer.analyze(source_code_paths)
    
    # Step 3: Scan for vulnerabilities
    
    vulnerabilities = []
    for url in crawled_urls:
        response = http_client.send_request(url)
        detected_vulnerabilities = vulnerability_scanner.scan(response)
        vulnerabilities.extend(detected_vulnerabilities)
    
    # Step 4: Perform dynamic analysis
    
    dynamic_analysis_results = dynamic_analyzer.analyze(target_url)
    
    # Step 5: Generate vulnerability report

    report = report_generator.generate_report(
        crawled_urls, static_analysis_results, vulnerabilities, dynamic_analysis_results
    )
    report.save("vulnerability_report.html")

if __name__ == "__main__":
    main()
