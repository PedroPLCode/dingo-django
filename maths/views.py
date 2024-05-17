from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib import messages
from maths.models import Math, Result
from maths.forms import ResultForm

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
 
	result = Result.objects.get_or_create(value=(a+b))[0]
	Math.objects.create(operation='add', a=a, b=b, result=result)
 
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
 
	result = Result.objects.get_or_create(value=(a-b))[0]
	Math.objects.create(operation='sub', a=a, b=b, result=result)
 
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
 
	result = Result.objects.get_or_create(value=(a*b))[0]
	Math.objects.create(operation='mul', a=a, b=b, result=result)
 
	return render(
    	    request=request,
    	    template_name="maths/operation.html",
    	    context=c
	)


def div(request, a, b):
    
    if int(b) == 0:
        messages.add_message(request, messages.ERROR, "Dzielenie przez zero!")
        
    a, b = int(a), int(b)
    c = {
        "a":str(a),
        "b":str(b),
        "operacja": "/",
        "wynik":str(a/b) if b != 0 else None,
        "title": "dzielenie",
        }

    result = Result.objects.get_or_create(value=(a/b))[0]
    Math.objects.create(operation='div', a=a, b=b, result=result)
 
    return render(
		request=request,
		template_name="maths/operation.html",
		context=c
	)
    

def maths_list(request):
    maths = Math.objects.all()
    page_number = request.GET.get('page')
    operation_filter = request.GET.get('operation')
    
    if operation_filter:
        maths = Math.objects.filter(operation=operation_filter)
        
    paginator = Paginator(maths, 5)
    maths = paginator.get_page(page_number)
        
    return render(
        request=request,
        template_name="maths/list.html",
        context={"maths": maths,
                 "operation_filter": operation_filter,
                }
    )


def math_details(request, id):
   math = Math.objects.get(id=id)
   return render(
       request=request,
       template_name="maths/details.html",
       context={"math": math}
   )
   
   
def results_list(request):
    if request.method == "POST":
        form = ResultForm(data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Result added successfully")
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors['__all__']
            )

    form = ResultForm()
    results = Result.objects.all()
    return render(
        request=request,
        template_name="maths/results.html",
        context={
            "results": results,
            "form": form,
        }
    )