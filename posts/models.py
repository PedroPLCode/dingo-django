from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30, unique=True, null=False)
    content = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        'posts.Author',
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    
    def __str__(self):
        return (f"id:{self.id}\n"
                f"title={self.title}\n"
                f"content={self.content}\n"
                f"created={self.created}\n"
                f"modified={self.modified}\n")


class Author(models.Model):
    nick = models.CharField(max_length=30, null=False, unique=True)
    email = models.EmailField(null=False, unique=True)
    
    def __str__(self):
        return (f"id:{self.id}\n"
                f"nick={self.nick}\n"
                f"email={self.email}\n")