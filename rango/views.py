from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    #return HttpResponse("Rango says hey there world! <br/> <a href='/rango/about'>About</a>")
    context_dict = {'boldmessage':" I am bold font from the context"}
    return render(request, 'rango/index.html', context_dict)

    
def about(request):
    return HttpResponse("Rango says here is the about page. </br><a href='/rango/'>Index</a>")