from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>home</h1>")

def about(request):
    return HttpResponse("<h1>about</h1>")

def services(request):
    return HttpResponse("<h1>services</h1>")

def store(request):
    return HttpResponse("<h1>store</h1>")

def contact(request):
    return HttpResponse("<h1>contact</h1>")

def blog(request):
    return HttpResponse("<h1>blog</h1>")

def sample(request):
    return HttpResponse("<h1>sample</h1>")

