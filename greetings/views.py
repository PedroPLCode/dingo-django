from django.shortcuts import render
from django.http import HttpResponse

def show_greetings(request, name=None):
    return HttpResponse(f'Hello {name.title() if name else "World"}!')