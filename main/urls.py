from django.urls import path

from . views import *

app_name = "main"

urlpatterns = [
    path('', home, name='home'),
    path('front-page/', frontpage, name='front-page'),
    path('rooms/', xonalar, name='xonalar'),
    path('<slug:slug>/', xona, name='xona')
]
