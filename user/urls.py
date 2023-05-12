from django.urls import path
from . import views

# 127.0.0.1:8000/login

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]