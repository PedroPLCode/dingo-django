from django.shortcuts import render
from django.http import HttpResponse

def show_greetings(request, name=None):
	c = {"name": name if name else "world"}
	return render(
    	    request=request,
    	    template_name="greetings/main.html",
    	    context=c
	)