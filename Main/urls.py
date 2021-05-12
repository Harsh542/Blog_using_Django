from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('<slug:slug>/', views.post_detail,name="post_detail"),
    path('/Add_Post/', views.Add_Post, name="Add_Post"),
    path('delete/<email>/<slug:slug>/', views.delete, name="delete"),
]
