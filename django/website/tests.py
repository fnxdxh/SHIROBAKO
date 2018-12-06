from django.test import TestCase
from django.test.client import Client
import unittest
# Create your tests here.


class TestRegister(unittest.TestCase):
    def test_competitor_register(self):
        c = Client()
        response = c.post('/register/', {'username': 'john', 'password': 'smith'})
        self.assertEqual(response, {'msg': 'success', 'error_num': 0})
