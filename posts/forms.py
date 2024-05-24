from django import forms
from posts.models import Author, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        fields = ["title", "content", "author",  "tags", "image"]
        
    image = forms.ImageField(required=False)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        author = cleaned_data.get('author')

        if not (title and content and author):
            raise forms.ValidationError("Wypelnij wszystkie pola")
       

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['nick', 'email']

    def clean(self):
        cleaned_data = super().clean()
        nick = cleaned_data.get('nick')
        email = cleaned_data.get('email')

        if not (nick and email):
            raise forms.ValidationError("Podaj nick oraz email")