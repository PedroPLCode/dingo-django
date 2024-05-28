from django.contrib import admin
from books.models import Book, Author, Tag

class BookAdmin(admin.ModelAdmin):
   list_display = ["id", "title", "comment", "author"]
   list_filter = ["title"]
   search_fields = ["title", "comment"]

admin.site.register(Book, BookAdmin)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
   list_display = ['id', 'name', "comment"]
   list_filter = ["name"]
   search_fields = ["name"]
   
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
   list_display = ['id', 'word']
   list_filter = ["word"]
   search_fields = ["word"]