from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home),
    path('',views.home),
    path('register', views.register),
    path('login', views.login_view),
    path('task_view',views.task_create_view),
    path('welcome', views.welcome_user),
    path('logout',views.logout_view),
]