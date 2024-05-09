from django.contrib import admin
from posts.models import Post, Author

class PostAdmin(admin.ModelAdmin):
   list_display = ["id", "title", "content", "created", "modified", "author"]
   list_filter = ["title"]
   search_fields = ["title", "content"]

admin.site.register(Post, PostAdmin)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
   list_display = ['id', 'nick', 'email']
   list_filter = ["nick"]
   search_fields = ["nick"]