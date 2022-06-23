from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from PFC.views import index, about_us, bd

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index/', index),
    path('Noticias/', include('blog.urls')),
    path('Cuenta/', include('Accounts.urls')),
    path('about-us/', about_us),
    path('bd/', bd, name = 'bd'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)