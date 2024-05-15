from django.test import TestCase, Client
        
class MathViewsTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_default_greetings(self):
        response = self.client.get("/greetings/")
        self.assertEqual(response.status_code, 200)
        self.assertIn('<h3>Hello World!</h3>', response.content.decode())

    def test_name_greetings(self):
        response = self.client.get("/greetings/pedro")
        self.assertEqual(response.status_code, 200)
        self.assertIn('<h3>Hello Pedro!</h3>', response.content.decode())