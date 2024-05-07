from django.urls import path
from .views import show_greetings

urlpatterns = [
   path('', show_greetings),
   path('<name>', show_greetings)
]