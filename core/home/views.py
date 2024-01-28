from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):
    # template engine to show whatever data we have here or coming from the backend which has to be shown in our html page we use context for that. Let's see
    peoples = [
        {'name': 'Bhanu Teja', 'age': 21},
        {'name': 'Bhanu Prasad', 'age': 22},
        {'name': 'Yekaditya', 'age': 16},
        {'name': 'Venkat', 'age': 21},
        {'name': 'Phani', 'age': 12},
    ]
    
    vegetables = [
        'pumpkin', 'tomato', 'potato'
    ]
    return render(request, "home/index.html", context={'peoples': peoples, 'vegetables': vegetables})
def success_page(request):
    return HttpResponse("<h1> This is a Success Page </h1>")

def about(request):
    return render(request, "home/about.html")

def contact(request):
    return render(request, "home/contact.html")