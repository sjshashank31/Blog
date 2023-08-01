from django.contrib import admin

# Register your models here.
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(Blog, BlogAdmin)
