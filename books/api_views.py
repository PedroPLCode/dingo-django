from rest_framework.viewsets import ModelViewSet

from books.models import Book, Author, Comment, Borrow
from books.serializers import BookSerializer, BookAuthorSerializer, BookCommentSerializer, BookBorrowSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
class BookAuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = BookAuthorSerializer
    
class BookCommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = BookCommentSerializer
    
class BookBorrowViewSet(ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BookBorrowSerializer