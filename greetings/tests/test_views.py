from django.test import TestCase
        
class GreetingsViewsTest(TestCase):

    def test_default_greetings(self):
        response = self.client.get("/greetings/")
        self.assertEqual(response.status_code, 200)
        self.assertIn('<h3>Hello World!</h3>', response.content.decode())

    def test_specified_greetings(self):
        response = self.client.get("/greetings/pedro")
        self.assertEqual(response.status_code, 200)
        self.assertIn('<h3>Hello Pedro!</h3>', response.content.decode())