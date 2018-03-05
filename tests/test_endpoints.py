import unittest
from example.api.auth import hello
from example.app import app
import json

class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.dummy_post_man = app.test_client()

    def test_return_helloworld(self):
        response = self.dummy_post_man.get('/hello')
        self.assertEqual(json.loads(response.data)['hello'], 'world')

    def test_test(self):
        pass

    def tearDown(self):
        pass
