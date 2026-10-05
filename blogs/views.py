from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Blog,Category

# Gets the category ID from the URL
def posts_by_category(request,category_id):
    #Fetch the posts that belongs to the category with the category_id
    posts =  Blog.objects.filter(status='Published',category=category_id)
    # Use try/except when we wnt to do some custom action if the category does not exists
    try:
        category = Category.objects.get(pk=category_id)
    except:
        # redirect user to home page
        return redirect('home')
    # Use get_objects_or_404 when you want to show 404 error page if the category does not exists  
    # category = get_object_or_404(Category,pk=category_id)
    
    context = {
        'posts' : posts,
        'category' : category
    }
    return render(request,'posts_by_category.html',context)