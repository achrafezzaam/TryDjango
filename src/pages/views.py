from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {"title": 'Home page'})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {"title": 'About us'})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {"title": 'Contact us'})