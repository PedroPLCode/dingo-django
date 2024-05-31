from rest_framework import routers
from posts import api_views as posts_views
from books import api_views as books_views

posts_router = routers.DefaultRouter()
posts_router.register(r'posts', posts_views.PostViewSet, basename='post')
posts_router.register(r'authors', posts_views.PostAuthorViewSet, basename='postauthor')

books_router = routers.DefaultRouter()
books_router.register(r'books', books_views.BookViewSet, basename='book')
books_router.register(r'authors', books_views.BookAuthorViewSet, basename='bookauthor')
books_router.register(r'comments', books_views.BookCommentViewSet, basename='bookscomments')
books_router.register(r'borrows', books_views.BookBorrowViewSet, basename='booksborrows')
