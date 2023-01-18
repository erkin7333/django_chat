import requests
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


app_name = 'accaunts'

urlpatterns = [
    path('registr/', views.register, name='registr'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]