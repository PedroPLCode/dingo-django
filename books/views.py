from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Count
from books.models import Book, Author, Tag

def books_list(request):
    page_number = request.GET.get('page')
    books_filter = request.GET.get('filter')
    
    if books_filter:
        books = Book.objects.filter(title__icontains=books_filter)
    else:
        books = Book.objects.all()
        
    paginator = Paginator(books, 5)
    books = paginator.get_page(page_number)
    return render(
        request=request,
        template_name="books/books_list.html",
        context={"books": books,
                 "books_filter": books_filter,
                }
    )


def book_details(request, id):
    book = Book.objects.get(id=id)

    return render(
        request=request,
        template_name="books/book_details.html",
        context={"book": book}
    )
   

def authors_list(request):
    page_number = request.GET.get('page')
    author_filter = request.GET.get('filter')

    if author_filter:
        authors = Author.objects.filter(name__icontains=author_filter).annotate(book_count=Count('book'))
    else:
        authors = Author.objects.annotate(book_count=Count('book'))
        
    paginator = Paginator(authors, 5)
    authors = paginator.get_page(page_number)
    return render(
        request=request,
        template_name="books/authors_list.html",
        context={"authors": authors,
                 "author_filter": author_filter,
                 }
    )


def author_details(request, id):
    author = Author.objects.get(id=id)
    author_books = Book.objects.filter(author__name=author.name)

    return render(
        request=request,
        template_name="books/author_details.html",
        context={"author": author,
                 "author_books": author_books,
                 }
    )
    
    
def author_books(request, name):
    page_number = request.GET.get('page')
    author = get_object_or_404(Author, name__icontains=name)
    books = Book.objects.filter(author__name__icontains=name)
    paginator = Paginator(books, 5)
    books = paginator.get_page(page_number)
    return render(
        request=request,
        template_name="books/books_list.html",
        context={"books": books, "author": author,
        }
    )
    
    
def books_with_tag(request, tag):
    page_number = request.GET.get('page')
    tag = get_object_or_404(Tag, word=tag)
    books = Book.objects.filter(tags=tag)
    paginator = Paginator(books, 5)
    books = paginator.get_page(page_number)
    return render(
        request=request,
        template_name="books/books_list.html",
        context={"books": books, "tag": tag,
        }
    )