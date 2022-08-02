from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from myapp.models import Blog, Comment

# Create your views here.
def index(request):
    blog=Blog.objects.all() 
    return render (request,"index.html" , {'blog':blog})

def blog(request,pk):
    blog =Blog.objects.get(id=pk)
   
    return render(request,"blog.html" , {'blog' : blog})

def comment(request):
    comment=Comment.objects.all()
    print(comment)

    return HttpResponse("comments")
