from django.urls import path
from .views import posts_list, post_details, authors_list, author_details, author_posts, posts_with_tag

app_name="posts"
urlpatterns = [
   path('list/', posts_list, name="list"),
   path('list/<str:nick>', author_posts, name="author_posts"),
   path('tag/<str:tag>/', posts_with_tag, name='posts_with_tag'),
   path('details/<int:id>', post_details, name="details"),
   path('authors/', authors_list, name="authors"),
   path('authordetails/<int:id>', author_details, name="authordetails"),
]