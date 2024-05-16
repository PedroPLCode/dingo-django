from django.test import TestCase
from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm

class PostFormTest(TestCase):
    
    def setUp(self):
        Author.objects.create(nick="test nick 1", email="test@email.com")

    def test_post_save_correct_data(self):
        author = Author.objects.get(nick="test nick 1")
        data = {"title": "test title", "content": "test content", "author": author.id}
        self.assertEqual(len(Post.objects.all()), 0)
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())
        p = form.save()
        self.assertIsInstance(p, Post)
        self.assertEqual(p.title, "test title")
        self.assertEqual(p.content, "test content")
        self.assertEqual(p.author.id, author.id)
        self.assertIsNotNone(p.id)
        self.assertIsNotNone(p.created)
        self.assertIsNotNone(p.modified)


class AuthorFormTest(TestCase):

    def test_author_save_correct_data(self):
        data = {"nick": "test nick", "email": "test@email.com"}
        self.assertEqual(len(Post.objects.all()), 0)
        form = AuthorForm(data=data)
        self.assertTrue(form.is_valid())
        a = form.save()
        self.assertIsInstance(a, Author)
        self.assertEqual(a.nick, "test nick")
        self.assertEqual(a.email, "test@email.com")
        self.assertIsNotNone(a.id)