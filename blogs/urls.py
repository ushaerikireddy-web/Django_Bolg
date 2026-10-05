from django.urls import include, path

from . import views



urlpatterns = [
    path('<int:category_id>/',views.posts_by_category,name='posts_by_category')
    # Gets the category ID from the URL and shows the posts of that category

]
