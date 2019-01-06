from django.urls import path
from app01 import views

urlpatterns = [
    path('', views.user, name='user'),
    path('login/', views.login, name='login'),
    path('add/', views.users_add, name='add'),
    path('edit/', views.users_edit, name='users_edit'),
    path('role/', views.role, name='role'),
    path('role/add/', views.role_add, name='role_add'),
]
