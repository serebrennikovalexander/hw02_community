from django.conf import settings
from django.shortcuts import get_object_or_404, render

from .models import Group, Post


# Главная страница
def index(request):
    posts = Post.objects.order_by('-pub_date')[:settings.NUMBER_OF_POSTS]
    template = 'posts/index.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.order_by('-pub_date')[:settings.NUMBER_OF_POSTS]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
