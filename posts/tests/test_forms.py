from django.test import TestCase
from posts.models import Post, Author
from posts.forms import PostForm, AuthorForm

class PostFormTest(TestCase):

    def test_post_save_correct_data(self):
        data = {"title": "test title", "content": "test content", "author": 3}
        self.assertEqual(len(Post.objects.all()), 0)
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())
        p = form.save()
        self.assertIsInstance(p, Post)
        self.assertEqual(p.title, "test title")
        self.assertEqual(p.content, "test content")
        self.assertEqual(p.author, 3)
        self.assertIsNotNone(p.id)
        self.assertIsNotNone(p.created)
        self.assertIsNotNone(p.modified)


class AuthorFormTest(TestCase):

    def test_author_save_correct_data(self):
        data = {"nick": "test nick", "email": "test email"}
        self.assertEqual(len(Post.objects.all()), 0)
        form = AuthorForm(data=data)
        self.assertTrue(form.is_valid())
        a = form.save()
        self.assertIsInstance(a, Author)
        self.assertEqual(a.nick, "test nick")
        self.assertEqual(a.email, "test email")
        self.assertIsNotNone(a.id)
        self.assertIsNotNone(a.created)
        self.assertIsNotNone(a.modified)