from unittest import TestCase
from django.urls import resolve
from greetings.views import show_greetings

class TestUrls(TestCase):
   def test_resolution_for_default_greetings(self):
       resolver = resolve('/greetings/')
       self.assertEqual(resolver.func, show_greetings)

   def test_resolution_for_specified_greetings(self):
       resolver = resolve('/greetings/pedro')
       self.assertEqual(resolver.func, show_greetings)