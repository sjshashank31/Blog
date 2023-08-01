from django.shortcuts import render, HttpResponse, redirect
from .models import Blog
from .forms import BlogForm
from django.urls import reverse
# Create your views here.


def blog_listing(request, *args, **kwargs):
    blogs = Blog.objects.all()
    return render(request, "blog_listing.html", {'blogs': blogs})

def blog_detail(request, *args, **kwargs):
    blog = Blog.objects.get(slug=kwargs.get("slug"))
    print(blog)
    return render(request, 'blog_detail.html', {'blog': blog})


def update_blog(request, *args, **kwargs):
    slug = kwargs.get('slug')
    blog = Blog.objects.get(slug=slug)
    form = BlogForm(request.POST or None, instance=blog)

    if form.is_valid():
        print("Form is Valid")
        form.save()
        return redirect('blog_listing')

    form = BlogForm(request.POST or None, instance=blog)
    return render(request, 'blog_update.html', {'form': form})



def create_blog(request, *args, **kwargs):
    pass
