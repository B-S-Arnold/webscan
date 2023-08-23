import requests

class HTTPClient:
    def __init__(self):
        self.session = requests.Session()

    def get(self, url):
        response = self.session.get(url)
        return response

    def post(self, url, data=None):
        response = self.session.post(url, data=data)
        return response

    def send_request(self, method, url, data=None):
        if method == "GET":
            return self.get(url)
        elif method == "POST":
            return self.post(url, data=data)
        else:
            raise ValueError("Unsupported HTTP method")

    def close(self):
        self.session.close()
