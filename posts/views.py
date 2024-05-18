from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from posts.models import Post, Author
from posts.forms import AuthorForm, PostForm

def posts_list(request):
    page_number = request.GET.get('page')
    post_filter = request.GET.get('filter')
    
    if request.method == "POST":
        form = PostForm(data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Post added successfully")
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors['__all__']
            )
            
    form = PostForm()
    
    if post_filter:
        posts = Post.objects.filter(title__icontains=post_filter)
    else:
        posts = Post.objects.all()
        
    paginator = Paginator(posts, 5)
    posts = paginator.get_page(page_number)
    return render(
        request=request,
        template_name="posts/list.html",
        context={"posts": posts,
                 "form": form,
                 "post_filter": post_filter,
                }
    )


def post_details(request, id):
    post = Post.objects.get(id=id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post changed successfully")
    else:
        form = PostForm(instance=post) 

    return render(
        request=request,
        template_name="posts/details.html",
        context={"post": post, "form": form}
    )
   

def authors_list(request):
    page_number = request.GET.get('page')
    author_filter = request.GET.get('filter')
    
    if request.method == "POST":
        form = AuthorForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Author added successfully")
            return redirect('posts:authors')
        else:
            if '__all__' in form.errors:
                error_message = form.errors['__all__']
            else:
                error_message = "Something went wrong"
            messages.error(request, error_message)

    else:
        form = AuthorForm()

    if author_filter:
        authors = Author.objects.filter(nick__icontains=author_filter)
    else:
        authors = Author.objects.all()
        
    paginator = Paginator(authors, 5)
    authors = paginator.get_page(page_number)
    return render(
        request=request,
        template_name="posts/authors.html",
        context={"authors": authors,
                 "form": form,
                 "author_filter": author_filter,
                 }
    )


def author_details(request, id):
    author = Author.objects.get(id=id)
    
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            messages.success(request, "Author changed successfully")
    else:
        form = AuthorForm(instance=author) 

    return render(
        request=request,
        template_name="posts/authordetails.html",
        context={"author": author,
                 "form": form,
                }
    )