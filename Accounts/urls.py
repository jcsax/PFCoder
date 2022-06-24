from django.urls import path
from Accounts.views import login_view, logout_view, register_view, contact_view
from users.views import profile_view

urlpatterns = [
    path('iniciar-sesion/', login_view, name = 'login'),
    path('cerrar-sesion/', logout_view, name = 'logout'),
    path('registrarse/', register_view, name = 'register'),
    path('contacto/', contact_view, name = 'contact_form'),
    path('<int:pk>/', profile_view.as_view(), name = 'profile_view'),
    
]