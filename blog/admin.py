from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'photo', 'views', 'publication_date', )
    search_fields = ('title', 'publication_date',)


def my_media(data):
    if data:
        return f'media/blog/photo/{data}'
    return f'media/blog/photo/empty.pic.jpg'
