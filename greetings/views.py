from django.shortcuts import render
from django.http import HttpResponse

def show_greetings(request, name=None):
	c = {"name":name.title() if name else "World"}
	return render(
    	    request=request,
    	    template_name="greetings/main.html",
    	    context=c
	)