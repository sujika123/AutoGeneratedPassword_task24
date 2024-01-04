from django.urls import path

from demoapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('password/', views.password, name="password"),

]






