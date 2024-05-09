from django.shortcuts import render, redirect
from django.contrib import messages
from posts.models import Post, Author
from posts.forms import AuthorForm, PostForm

def posts_list(request):
    if request.method == "POST":
        form = PostForm(data=request.POST)

        if form.is_valid():
            Post.objects.get_or_create(**form.cleaned_data)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Utworzono nowy post"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors['__all__']
            )
            
    posts = Post.objects.all()
    form = PostForm()
    return render(
        request=request,
        template_name="posts/list.html",
        context={"posts": posts,
                 "form": form,
                }
    )


def post_details(request, id):
    post = Post.objects.get(id=id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
    else:
        form = PostForm(instance=post) 

    return render(
        request=request,
        template_name="posts/details.html",
        context={"post": post, "form": form}
    )
   

def authors_list(request):
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

    authors = Author.objects.all()
    return render(
        request=request,
        template_name="posts/authors.html",
        context={"authors": authors, "form": form}
    )


def author_details(request, id):
    author = Author.objects.get(id=id)
    
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
    else:
        form = AuthorForm(instance=author) 

    return render(
        request=request,
        template_name="posts/authordetails.html",
        context={"author": author,
                 "form": form,
                }
    )