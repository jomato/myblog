from django.shortcuts import render, get_object_or_404
from . models import Post, Category
import markdown

# Create your views here.


def index(request):
    post_list = Post.objects.all().order_by('-modified_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()#阅读量增加
    post.body = markdown.markdown(post.body, extensions=['markdown.extensions.extra',
                                                         'markdown.extensions.codehilite',
                                                         'markdown.extensions.toc',
                                                         ])
    return render(request, 'blog/detail.html', context={'post': post})


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month).order_by('-modified_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = Category.objects.filter(pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-modified_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})