from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from PFC.views import index, about_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index/', index),
    path('noticias/', include('blog.urls')),
    path('cuenta/', include('Accounts.urls')),
    path('sobre-nosotros/', about_us),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)