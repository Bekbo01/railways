from django.contrib import admin
from django.urls import re_path, path

from user_authentication import views

urlpatterns = [
    re_path(r'home/?',  views.home, name='home'),
    re_path('login/?', views.login_user, name='login'),
    re_path('register/?', views.register, name='register'),
    re_path('logout/?', views.logout_user, name='logout'),
    
    path("password_reset", views.password_reset_request, name="password_reset")
]