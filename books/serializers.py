from rest_framework import serializers

from books.models import Book, Comment, Author, Tag, Borrow

class BookSerializer(serializers.ModelSerializer):
   class Meta:
       model = Book
       fields = ('id', 'title', 'comment', 'pages', 'image', 'author', 'tags')

class BookAuthorSerializer(serializers.ModelSerializer):
   class Meta:
       model = Author
       fields = ('id', 'name', 'comment')

class BookTagSerializer(serializers.ModelSerializer):
   class Meta:
       model = Tag
       fields = ('id', 'word')
       
class BookCommentSerializer(serializers.ModelSerializer):
   class Meta:
       model = Comment
       fields = ('id', 'author', 'comment', 'book')
       
class BookBorrowSerializer(serializers.ModelSerializer):
   class Meta:
       model = Borrow
       fields = ('id', 'borrow_date', 'return_date', 'is_returned', 'comment', 'book', 'user')