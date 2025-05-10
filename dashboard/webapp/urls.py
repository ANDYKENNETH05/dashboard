from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),
    path("register", views.register, name="register"),
    path("my-login", views.myLogin, name = "my-login"),
    path("user-logout", views.user_logout, name = "user-logout"),
    path("dasboard", views.dashboard, name = "dashboard"),
    
    path('dashboard', views.dashboard, name = "dasboard"),
 
    path('create-record',views.create_record, name ='create-record'),
    path('update-record/<int:pk>',views.update_record, name ='update-record'),
    path('record/<int:pk>', views.view_record, name = 'record'),
    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),
]