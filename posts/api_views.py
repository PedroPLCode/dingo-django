from rest_framework.viewsets import ModelViewSet

from posts.models import Post, Author
from posts.serializers import PostSerializer, PostAuthorSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostAuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = PostAuthorSerializer