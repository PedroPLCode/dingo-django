from django.contrib import admin
from books.models import Book, Author, Tag, Borrow

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
   
@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
   list_display = ['id', 'comment', 'book', 'user', 'borrow_date', 'return_date', 'is_returned']
   list_filter = ["book", "user"]
   search_fields = ["book", "user", "comment"]