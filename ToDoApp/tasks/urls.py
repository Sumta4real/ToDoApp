from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home, name='home'),
    path('',views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('create_task',views.create_task, name='create_task'),
    path('welcome', views.welcome_user, name='welcome'),
    path('logout',views.logout_view, name='logout'),
    path('tasks_list',views.tasks_list, name='tasks_list'),
    path('update_task/<str:task_id>', views.update_task, name='update_task'),
    path('delete_task/<str:task_id>', views.delete_task, name='delete_task'),
]