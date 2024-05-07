from django.shortcuts import render
from django.http import HttpResponse

def math(request):
   return HttpResponse("Tu będzie matma")


def add(request, a, b):
	a, b = int(a), int(b)
	c = {
    	"a":str(a), 
      	"b":str(b), 
      	"operacja": "+",
      	"wynik":str(a+b), 
      	"title": "dodawanie"
       }
	return render(
    	    request=request,
    	    template_name="maths/operation.html",
    	    context=c
	)


def sub(request, a, b):
	a, b = int(a), int(b)
	c = {
     	"a":str(a),
      	"b":str(b),
       	"operacja": "-",
        "wynik":str(a-b),
        "title": "odejmowanie"
        }
	return render(
    	    request=request,
    	    template_name="maths/operation.html",
    	    context=c
	)


def mul(request, a, b):
	a, b = int(a), int(b)
	c = {"a":str(a),
      	"b":str(b),
      	"operacja": "*",
      	"wynik":str(a*b),
      	"title": "mnozenie"
     	}
	return render(
    	    request=request,
    	    template_name="maths/operation.html",
    	    context=c
	)


def div(request, a, b):
    a, b = int(a), int(b)
    c = {
        "a":str(a),
        "b":str(b),
        "operacja": "/",
        "wynik":str(a/b) if b != 0 else None,
        "title": "dzielenie",
        }
    return render(
		request=request,
		template_name="maths/operation.html",
		context=c
	)