from rest_framework.viewsets import ModelViewSet

from posts.models import Post, Author
from posts.serializers import PostSerializer, AuthorSerializer

class PostViewset(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class AuthorViewset(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer