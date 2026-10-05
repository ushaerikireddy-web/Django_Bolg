


from django.shortcuts import render

from django.http import HttpResponse
from blogs.models import Blog, Category


def home(request):
    featured_posts = Blog.objects.filter(is_featured=True , status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False,status='Published')
    print("FEATURED POSTS:", featured_posts)
    print("RECENT POSTS:", posts)
    context ={
        'featured_posts' : featured_posts,
        'posts' : posts,
    }
    return render(request,'home.html',context)