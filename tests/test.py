import unittest
import requests


# def addTwoNumbers(a, b):
#     return a+b
#
#
# class AddTest(unittest.TestCase):
#     def test1(self):
#         c = addTwoNumbers(5, 10)
#         self.assertEqual(c, 15)
#
#     def test2(self):
#         c = addTwoNumbers(5, 10)
#         self.assertNotEqual(c, 10)

class ApiTest(unittest.TestCase):
    # api = "http://127.0.0.1:5000/articles/"
    api = "http://127.0.0.1:5000/articles"

    # ARTICLE_URL = "/articles/{}/".format(api)

    def test1(self):
        r = requests.get(ApiTest.api)
        self.assertEqual(r.status_code, 200)
        # self.assertEqual(len(r.json()), 2)





if __name__ == "__main__":
    unittest.main()
