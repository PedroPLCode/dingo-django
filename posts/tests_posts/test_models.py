from django.test import TestCase
from posts.models import Post, Author

class PostModelTest(TestCase):

    def setUp(self):
        Author.objects.create(nick="test nick 1", email="test@email.com")
        author = Author.objects.get(nick="test nick 1")
        Post.objects.create(title="test title 7", content="test content 7", author=author)

    def test_post_str(self):
        p = Post.objects.get(title="test title 7")
        author = Author.objects.get(nick="test nick 1")
        self.assertEqual(str(p), f'id:{author.id} test title 7')
        
        
class AuthorModelTest(TestCase):

    def setUp(self):
        Author.objects.create(nick="test nick 1", email="test email 1")

    def test_author_str(self):
        a = Author.objects.get(nick="test nick 1")
        self.assertEqual(str(a), f'id:{a.id} test nick 1')