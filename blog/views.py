from django.shortcuts import render
from .models import Post

# Create your views here.


def blog_main(request):
    return render(request, 'blog_main.html')


def blog_post(request):
    postlist = Post.objects.all()
    return render(request, 'blog_post.html', {'postlist': postlist})


def blog_post_category(request, category):
    postlist = Post.objects.filter(categorys=category)
    return render(request, 'blog_post.html', {'postlist': postlist})


def blog_post_view(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog_post_view.html',{'post': post})