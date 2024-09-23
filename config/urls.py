from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('mail.urls', 'mail'), namespace='mail')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
