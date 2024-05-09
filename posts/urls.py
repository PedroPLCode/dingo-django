from django.urls import path
from .views import posts_list, post_details, authors_list, author_details

app_name="posts"
urlpatterns = [
   path('list/', posts_list, name="list"),
   path('details/<int:id>', post_details, name="details"),
   path('authors/', authors_list, name="authors"),
   path('authordetails/<int:id>', author_details, name="authordetails"),
]