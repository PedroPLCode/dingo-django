from unittest import TestCase
from django.urls import resolve
from django.urls.exceptions import Resolver404
from posts.views import posts_list, post_details, authors_list, author_details

class TestUrls(TestCase):
    
    def test_resolution_for_list(self):
        resolver = resolve('/posts/list/')
        self.assertEqual(resolver.func, posts_list)

    def test_resolution_for_details(self):
        resolver = resolve('/posts/details/1')
        self.assertEqual(resolver.func, post_details)
       
    def test_resolution_for_authors(self):
        resolver = resolve('/posts/authors/')
        self.assertEqual(resolver.func, authors_list)
       
    def test_resolution_for_authordetails(self):
        resolver = resolve('/posts/authordetails/1')
        self.assertEqual(resolver.func, author_details)

    def test_arguments_should_be_integers_or_404(self):
        with self.assertRaises(Resolver404):
            resolve('/posts/authordetails/mickiewicz')