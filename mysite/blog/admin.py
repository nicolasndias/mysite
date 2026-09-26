from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status",)  # Make sure to include a comma to indicate it's a tuple with one element
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}  # Make sure to include a comma to indicate it's a tuple with one element

admin.site.register(Post, PostAdmin)