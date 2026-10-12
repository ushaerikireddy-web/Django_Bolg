from django.contrib import admin

from blogs.models import Category,Blog,About, SocialLink,Comment


# This class is used to customize the Blog model in the Django admin panel
class BlogAdmin(admin.ModelAdmin):

    # Automatically creates the slug from the blog title
    # Example: "My First Blog" → "my-first-blog"
    prepopulated_fields={'slug':('title',)}

    # Displays these fields as columns in the Blog list
    # in the Django admin panel
    list_display = ('title','category','author','status','is_featured')

    # Allows searching blogs using ID, title, category name, and status
    # category__category_name searches the category_name field from the related Category model
    search_fields = ('id','title','category__category_name','status')
    # Allows the selected field to be edited directly from the Blog list page
    list_editable = ('is_featured',)
    # Registers the Category model in the Django admin panel
    admin.site.register(Category)
    

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count ==0:
            return True
        return False
admin.site.register(About,AboutAdmin)

admin.site.register(SocialLink)

# Registers the Blog model in the Django admin panel
# BlogAdmin is used to apply the custom admin settings
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)