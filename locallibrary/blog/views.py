from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

# Create your views here.
posts  = [
    {
        'author':'CoreyMS',
        'title':'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018',
        'other':'america'
    },
]


def home(request):
    context = {
        'posts':Post.objects.all()
    }
    # return render(request, 'blog/home.html',context)
    return render(request, 'blog/mainPage.html',context)
    # return HttpResponse('<doctype>...')

def about(request):
    return render(request, 'blog/about.html',{'title':'about'})
    # return HttpResponse('<h1>Blog About</h1>')

def register(request):
    return render(request, 'blog/register.html')

def Login(request):
    return render(request, 'blog/Login.html')

def share(request):
    return render(request, 'blog/share.html')

def forgetPass(request):
    return render(request, 'blog/forgetPass.html')

def mainPage(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/mainPage.html',context)
