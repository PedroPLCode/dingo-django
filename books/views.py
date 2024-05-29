from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Count
from books.models import Book, Author, Tag, Borrow, Comment
from django.contrib.auth.models import User

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
    comments = Comment.objects.filter(book__id=id)
    current_borrow = book.borrows.filter(is_returned=False).first()
    is_borrowed = current_borrow is not None
    
    if request.method == 'POST':
        if 'return_book' in request.POST:
            borrow = get_object_or_404(Borrow, id=current_borrow.id)
            borrow.is_returned = True
            borrow.return_date = timezone.now()
            borrow.save()
        elif 'borrow_book' in request.POST:
            try:
                borrow = Borrow.objects.get(book__id=id)
                borrow.is_returned = False
                borrow.borrow_date = timezone.now()
                borrow.user = request.user,
                borrow.save()
            except:
                Borrow.objects.create(
                    book=book,
                    user=request.user,
                    borrow_date=timezone.now(),
                    is_returned=False
                )
        elif 'comment' in request.POST:
            Comment.objects.create(
                    book=book,
                    author=request.user if request.user.is_authenticated else request.POST.get('author'),
                    comment=request.POST.get('comment')
                )
        return redirect('books:book_details', id=id)

    return render(
        request=request,
        template_name="books/book_details.html",
        context={"book": book, 
                 "comments": comments,
                 "is_borrowed": is_borrowed, 
                 "current_borrow": current_borrow
                 }
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
    page_number = request.GET.get('page')
    author = Author.objects.get(id=id)
    books = Book.objects.filter(author__name=author.name)
    paginator = Paginator(books, 5)
    books = paginator.get_page(page_number)

    return render(
        request=request,
        template_name="books/author_details.html",
        context={"author": author,
                 "books": books,
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
     
    
def borrows_list(request, username):
    page_number = request.GET.get('page')
    user = get_object_or_404(User, username=username)
    
    borrows_to_return = Borrow.objects.filter(user=user, is_returned=False)
    paginator = Paginator(borrows_to_return, 5)
    borrows_to_return = paginator.get_page(page_number)
    
    borrows_returned = Borrow.objects.filter(user=user, is_returned=True)
    paginator = Paginator(borrows_returned, 5)
    borrows_returned = paginator.get_page(page_number)
    
    return render(
        request=request,
        template_name="books/borrows_list.html",
        context={"borrows_to_return": borrows_to_return,
                 "borrows_returned": borrows_returned,
                 "user": user,
                 }
    )


def borrow_details(request, id):
    borrow = get_object_or_404(Borrow, id=id)

    if request.method == 'POST' and 'borrow_id' in request.POST:
        borrow = Borrow.objects.get(id=request.POST['borrow_id'])
        borrow.is_returned = True
        borrow.return_date = timezone.now()
        borrow.save()
        return redirect('books:borrow_details', id=id)
    
    return render(
        request=request,
        template_name="books/borrow_details.html",
        context={"borrow": borrow,
                 }
    )