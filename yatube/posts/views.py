from django.conf import settings
from django.shortcuts import get_object_or_404, render

from .models import Group, Post

NUMBER_OF_POSTS = settings.NUMBER_OF_POSTS


# Главная страница
def index(request):
    posts = Post.objects.select_related('author').all()[:NUMBER_OF_POSTS]
    template = 'posts/index.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:NUMBER_OF_POSTS]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
