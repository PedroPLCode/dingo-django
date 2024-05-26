from django.shortcuts import render
from django.http import HttpResponse

def show_greetings(request, name=None):
    if name == 'about':
        return render(
            request=request,
            template_name="about.html",
        )
    elif name == 'contact':
        return render(
            request=request,
            template_name="contact.html",
        )     
    else:
        c = {"name": name}
        return render(
			request=request,
			template_name="greetings/greetings.html",
			context=c,
		)