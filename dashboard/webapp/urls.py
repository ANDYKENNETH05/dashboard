from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("my-login", views.myLogin, name = "my-login"),
    path("user-logout", views.user_logout, name = "user-logout"),
    path("dasboard", views.dashboard, name = "dashboard"),

]