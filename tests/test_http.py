import unittest
from scanner.http import HTTPClient
import requests
from unittest.mock import Mock


class TestHTTPClient(unittest.TestCase):
    def setUp(self):
        self.client = HTTPClient()

    def tearDown(self):
        self.client.close()

    def test_get_request(self):
        # Mock the response for the get method
        mock_response = Mock(spec=requests.Response)
        mock_response.status_code = 200
        mock_response.text = "Response content"
        self.client.session.get = Mock(return_value=mock_response)

        response = self.client.get("http://example.com")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Response content")

    def test_post_request(self):
        # Mock the response for the post method
        mock_response = Mock(spec=requests.Response)
        mock_response.status_code = 201
        mock_response.text = "Created"
        self.client.session.post = Mock(return_value=mock_response)

        response = self.client.post(
            "http://example.com", data={"key": "value"})

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.text, "Created")

    def test_send_request_invalid_method(self):
        with self.assertRaises(ValueError):
            self.client.send_request("INVALID", "http://example.com")


if __name__ == '__main__':
    unittest.main()
