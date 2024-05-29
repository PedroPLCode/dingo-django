from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=30, unique=True, null=False)
    comment = models.TextField(null=True)
    pages = models.IntegerField(null=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, default='')
    tags = models.ManyToManyField("books.Tag", related_name="books")
    author = models.ForeignKey(
        'books.Author',
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    
    def __str__(self):
        return (f"id:{self.id} {self.title}")


class Comment(models.Model):
    author = models.CharField(max_length=30, null=False)
    comment = models.TextField(null=False)
    
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='comments'
    )

    def __str__(self):
        return f"id:{self.id} comment:{self.comment}"
    

class Author(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True)
    comment = models.TextField(null=True)
    
    def __str__(self):
        return (f"id:{self.id} {self.name}")
    
    
class Tag(models.Model):
    word = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return (f"id:{self.id} #{self.word}")
    
    
class Borrow(models.Model):
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True)
    is_returned = models.BooleanField(default=False)
    comment = models.TextField(null=True)
    
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='borrows'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='borrows',
    )

    def __str__(self):
        return f"id:{self.id} book:{self.book.title} user:{self.user.username}"