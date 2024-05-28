from django.db import models

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


class Author(models.Model):
    name = models.CharField(max_length=30, null=False, unique=True)
    comment = models.TextField(null=True)
    
    def __str__(self):
        return (f"id:{self.id} {self.name}")
    
    
class Tag(models.Model):
    word = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return (f"id:{self.id} #{self.word}")