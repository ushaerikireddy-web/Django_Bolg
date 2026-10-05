from django.db import models
from django.contrib.auth.models import User


# This model is used to create and store blog categories
class Category (models.Model):

    # Stores the name of the category
    # unique=True means duplicate category names are not allowed
    category_name=models.CharField(max_length=50,unique=True)

    # Stores the date and time when the category is created
    created_at=models.DateTimeField(auto_now_add=True)

    # Automatically updates the date and time whenever the category is modified
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        # This gives the plural name for the Category model in the admin panel
        # Without this we get Categorys
        # By using this it shows Categories
        verbose_name_plural='categories'

    def __str__(self):
        # This returns the category name as a string
        # In the admin panel, it shows the category name
        # instead of showing Object 1, Object 2, etc.
        return self.category_name


# These are the available status choices for a blog
# 0 means Draft
# 1 means Published
STATUS_CHOICES=(
    ("Draft","Draft"),
    ("Published","Published")
)


# This model is used to create and store blog posts
class Blog(models.Model):

     # Stores the title of the blog
     title = models.CharField(max_length=100)
     # Stores the URL-friendly name of the blog
     # unique=True means duplicate slugs are not allowed
     # blank=True means this field can be left empty in the form
     slug =models.SlugField(max_length=150,unique=True,blank=True)
     # Connects the blog with a Category
     # on_delete=models.CASCADE means if a category is deleted,
     # its related blogs will also be deleted
    #  Django detects this category as category_id so we can use both category and category_id in usage
     category = models.ForeignKey(Category,on_delete=models.CASCADE)
     # Connects the blog with the Django User
     # This stores which user created the blog
     # If the user is deleted, the related blogs are also deleted
     author = models.ForeignKey(User,on_delete=models.CASCADE)
     # Stores the featured image of the blog
     # The image will be stored inside uploads/year/month/day
     featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
     # Stores a short description of the blog
     short_description = models.TextField(max_length=500)
     # Stores the main content/body of the blog
     blog_body = models.TextField(max_length=2000)
     # Stores the status of the blog
     # 0 = Draft
     # 1 = Published
     status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="Draft")
     # Stores whether the blog is a featured blog
     # False = Not featured
     # True = Featured
     is_featured = models.BooleanField(default=False)
     # Stores the date and time when the blog is created
     created_at = models.DateTimeField(auto_now_add=True)
     # Automatically updates the date and time whenever the blog is modified
     updated_at = models.DateTimeField(auto_now=True)
     
     def __str__(self):
         return self.title