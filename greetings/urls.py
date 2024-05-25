from django.urls import path
from django.views.generic import TemplateView
from .views import show_greetings

urlpatterns = [
   path('', show_greetings),
   path('<name>', show_greetings),
   path('about/', TemplateView.as_view(template_name="about.html")),
   path('contact/', TemplateView.as_view(template_name="contact.html")),
]