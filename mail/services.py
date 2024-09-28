from random import shuffle

from django.core.cache import cache

from blog.models import Blog
from config.settings import CACHE_ENABLED
from mail.models import Newsletter


def get_three_articles():
    """Получает три случайных статьи из блога"""

    blog = list(Blog.objects.all())
    shuffle(blog)
    return blog[:3]


def get_blog_posts():
    """Получает статьи блога из кэша. Если кэш пустой, то получает из БД"""
    if not CACHE_ENABLED:
        return get_three_articles()
    key = 'blog_list'
    posts = cache.get(key)
    if posts is not None:
        return posts
    posts = Blog.objects.order_by('?')[:3]
    cache.set(key, posts)
    return Blog.objects.order_by('?')[:3]
