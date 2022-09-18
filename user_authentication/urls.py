from django.contrib import admin
from django.urls import re_path, path

from user_authentication import views

urlpatterns = [
    re_path(r'home/?',  views.home, name='home'),
    re_path('login/?', views.login_user, name='login'),
    re_path('register/?', views.register, name='register'),
    re_path('logout/?', views.logout_user, name='logout'),
    path("profile/", views.profile, name="profile"),
    path("task/<int:pk>/", views.task, name="tasks"),

    path("task/<int:pk>/<int:pk_depo>/machine_approve/", views.machine_approve, name="machine_approve"),
    path("task/<int:pk>/<int:pk_depo>/machine_unapprove/", views.machine_unapprove, name="machine_unapprove"),
    path("task/<int:pk>/<int:pk_depo>/depo_approve/", views.depo_approve, name="depo_approve"),
    path("task/<int:pk>/<int:pk_depo>/depo_unapprove/", views.depo_unapprove, name="depo_unapprove"),


    
    path("password_reset", views.password_reset_request, name="password_reset")
]