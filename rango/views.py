from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rango.models import Category
from django.conf.urls.static import static

def homepage(request):
    return HttpResponse("Homepage"
                        "<br>"
                        "Rango says hey there partner!"
                        "<br>"
                        "<a href='/rango'>Rango</href>")
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    
    return  render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {}
    return render(request, 'rango/about.html', context=context_dict)



