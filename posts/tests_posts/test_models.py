from django.test import TestCase
from posts.models import Post, Author

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(title="test title 7", content="test content 7", author=7)

    def test_post_str(self):
        p = Post.objects.get(nick="test nick 1")
        self.assertEqual(str(p), 'id:1 test title 7')
        
        
class AuthorModelTest(TestCase):

    def setUp(self):
        Author.objects.create(nick="test nick 1", email="test email 1")

    def test_author_str(self):
        a = Author.objects.get(nick="test nick 1")
        self.assertEqual(str(a), 'id:1 test nick 1')