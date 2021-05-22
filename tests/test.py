import unittest
import requests


class ApiTest(unittest.TestCase):
    api = "http://127.0.0.1:5000/articles"



    def test1(self):
        r = requests.get(ApiTest.api)
        self.assertEqual(r.status_code, 200)


if __name__ == "__main__":
    unittest.main()
