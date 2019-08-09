from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    my_title = 'how ya doing'
    context = {"title": my_title, "my_list":[1,2,3,4,5]}
    return render(request, "home.html", context)

def about_page(request):
    my_title = 'About us'
    return render(request, 'about.html', {'title': my_title})

def contact_page(request):
    my_title = 'Contact us'
    return render(request, "hello.html", {'title': my_title})
