from rest_framework import serializers

from posts.models import Post, Author, Tag

class PostSerializer(serializers.ModelSerializer):
   class Meta:
       model = Post
       fields = ('id', 'title', 'content', 'created', 'modified', 'author', 'image', 'tags')

class PostAuthorSerializer(serializers.ModelSerializer):
   class Meta:
       model = Author
       fields = ('id', 'nick', 'email')

class PostTagSerializer(serializers.ModelSerializer):
   class Meta:
       model = Tag
       fields = ('id', 'word', 'created')