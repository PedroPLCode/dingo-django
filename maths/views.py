from django.shortcuts import render
from django.http import HttpResponse

def math(request):
   return HttpResponse("Tu będzie matma")

def add(request, a, b):
	a, b = int(a), int(b)
	c = {"a":str(a), "b":str(b), "operacja": "+" ,"wynik":str(a+b)}
	return render(
    	    request=request,
    	    template_name="maths/main.html",
    	    context=c
	)

def sub(request, a, b):
	a, b = int(a), int(b)
	c = {"a":str(a), "b":str(b), "operacja": "-" ,"wynik":str(a-b)}
	return render(
    	    request=request,
    	    template_name="maths/main.html",
    	    context=c
	)

def mul(request, a, b):
	a, b = int(a), int(b)
	c = {"a":str(a), "b":str(b), "operacja": "*" ,"wynik":str(a*b)}
	return render(
    	    request=request,
    	    template_name="maths/main.html",
    	    context=c
	)

def div(request, a, b):
   a, b = int(a), int(b)
   
   if b == 0:
      return HttpResponse("Nie dziel przez 0")
   
   c = {"a":str(a), "b":str(b), "operacja": "/" ,"wynik":str(a/b)}
   return render(
    	request=request,
      template_name="maths/main.html",
    	context=c
	)