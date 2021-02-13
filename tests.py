import unittest
import requests

class TestSum(unittest.TestCase):
    def setUp(self):
        self.endpoint = 'http://localhost:5000/sum'
        return super().setUp()

    def test_no_teen_1(self):
        response = requests.post(self.endpoint, json={"data": [1, 2, 3]})
        # print("response", response.json())
        self.assertEqual(response.json(), {"status": 200, "result": 6})

    def test_no_teen_2(self):
        response = requests.post(self.endpoint, json={"data": [2, 13, 1]})
        # print("response", response.json())
        self.assertEqual(response.json(), {"status": 200, "result": 3})

    def test_teen_1(self):
        response = requests.post(self.endpoint, json={"data": [2, 1, 14]})
        # print("response", response.json())
        self.assertEqual(response.json(), {"status": 200, "result": 3})

    def test_teen_except_1(self):
        response = requests.post(self.endpoint, json={"data": [2, 1, 15]})
        # print("response", response.json())
        self.assertEqual(response.json(), {"status": 200, "result": 18})

    def test_less_args(self):
        response = requests.post(self.endpoint, json={"data": [1, 2]})
        # print("response", response.json())
        self.assertEqual(response.json(), {"status": 400, "error": "Exactly 3 numbers are required"})

    def test_more_args(self):
        response = requests.post(self.endpoint, json={"data": [1, 2, 15, 5]})
        # print("response", response.json())
        self.assertEqual(response.json(), {"status": 400, "error": "Exactly 3 numbers are required"})

    def test_non_numeric(self):
        response = requests.post(self.endpoint, json={"data": [2, 1, "15"]})
        # print("response", response.json())
        self.assertEqual(response.json(), {"status": 400, "error": "All inputs must be numeric"}
)
    

if __name__ == "__main__":
    unittest.main()