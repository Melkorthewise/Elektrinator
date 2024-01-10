from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name="login"),
    path('main', views.main, name="main"),
    path('signUp', views.signUp, name="signUp")
]
