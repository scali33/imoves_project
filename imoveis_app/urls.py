from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login',views.login_page, name='login'),
    path('logout', views.exit_page, name='logout'),
    path('register', views.register_user, name='register'),
    path('register_casa', views.register_casa, name='register_casa')
]