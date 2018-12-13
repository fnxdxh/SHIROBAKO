from django.test import TestCase
from django.test.client import Client
import unittest
# Create your tests here.


class TestRegister(unittest.TestCase):
    def test_competitor_register(self):
        c = Client()
        response = c.post('/api/register_competitor/', {'username': 'competitor', 'password': '2018'})
        self.assertEqual(response.content, {'msg': 'success', 'error_num': 0})

    def test_organizer_register(self):
        c = Client()
        response = c.pose('api/register_organizer', {'username': 'organizer', 'password': '2018'})
        self.assertEqual(response.content, {'msg': 'success', 'error_num': 0})
