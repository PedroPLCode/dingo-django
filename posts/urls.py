from django.urls import path
from .views import posts_list, post_details, authors_list, author_details, author_posts, posts_with_tag
from django.views.generic import ListView
from posts.models import Post

app_name="posts"
urlpatterns = [
   path('list/', posts_list, name="list"),
   path('list/author/<str:nick>', author_posts, name="author_posts"),
   path('list/tag/<str:tag>/', posts_with_tag, name='posts_with_tag'),
   path('post/<int:id>', post_details, name="details"),
   path('authors/', authors_list, name="authors"),
   path('author/<int:id>', author_details, name="author"),
   path('postslist/', ListView.as_view(model=Post), name="posts_list"), # testowo ale breadcrumbs nie dziala
]