from django.contrib import admin
from .models import Post

# Register your models here.
'''
We are telling the Django admin site that our model is registered into the admin site using a
custom class that inherits from ModelAdmin. In this class, we can include information about how
to display the model in the admin site and how to interact with it. The list_display attribute
allows you to set the fields of your model that you want to display in the admin object list page.
'''

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

admin.site.register(Post, PostAdmin)
