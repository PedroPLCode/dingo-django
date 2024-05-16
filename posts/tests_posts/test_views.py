from django.test import TestCase, Client
from posts.models import Post, Author
        
class PostsViewsTest(TestCase):

    def setUp(self):
        Post.objects.create(title="test title 7", content="test content 7", author=1)
        Author.objects.create(nick="test nick 1", email="test email 1")
        self.client = Client()

    def test_posts_list(self):
        response = self.client.get("/posts/list/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["posts"]), 1)
        self.assertIn('<li><a href="/posts/details/1">test title 7</a></li>', response.content.decode())

    def test_post_details(self):
        response = self.client.get("/posts/details/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn('<td>test title 7</td>', response.content.decode())
        self.assertIn('<td>test content 7</td>', response.content.decode())
        self.assertIn('<td>1</td>', response.content.decode())
        self.assertIn('<td>test nick 1</td>', response.content.decode())
        self.assertIn('<td>test email 1</td>', response.content.decode())        

    def test_authors_list(self):
        response = self.client.get("/posts/authors/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["authors"]), 1)
        self.assertIn('<li><a href="/posts/authordetails/1">test nick 1</a></li>', response.content.decode())
        
    def test_author_details(self):
        response = self.client.get("/posts/authordetails/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn('<td>1</td>', response.content.decode())
        self.assertIn('<td>test nick 1</td>', response.content.decode())
        self.assertIn('<td>test email 1</td>', response.content.decode())  