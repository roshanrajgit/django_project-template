from django.urls import path

from . import views

urlpatterns =[
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("user_list", views.user_list, name="user_list")
]   