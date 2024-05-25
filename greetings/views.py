from django.shortcuts import render
from django.http import HttpResponse

def show_greetings(request, name=None):
    c = {"name": name}
    return render(
			request=request,
			template_name="greetings/greetings.html",
			context=c
	)