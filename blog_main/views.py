


from django.shortcuts import render

from django.http import HttpResponse
from blogs.models import Blog, Category,About


def home(request):
    featured_posts = Blog.objects.filter(is_featured=True , status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False,status='Published')
    print("FEATURED POSTS:", featured_posts)
    print("RECENT POSTS:", posts)
    #Fetch about us
    try:
        about = About.objects.first()
    except :
        about = None
    context ={
        'featured_posts' : featured_posts,
        'posts' : posts,
        'about' :about,
    }
    return render(request,'home.html',context)