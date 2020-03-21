from django.shortcuts import render
from .models import Post, Category

def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts':posts})

# Create your views here.
