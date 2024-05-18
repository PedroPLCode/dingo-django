from django.shortcuts import render
from django.http import HttpResponse

def show_greetings(request, name=None):
    
    if name == "contact":
        return render(
				request=request,
				template_name="greetings/contact.html",
		)
    elif name == "about":
        return render(
				request=request,
				template_name="greetings/about.html",
		)
    else:    
        c = {"name": name}
        return render(
				request=request,
				template_name="greetings/greetings.html",
				context=c
		)