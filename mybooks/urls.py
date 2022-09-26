from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path
from mybooks.views import login_view,register,home

urlpatterns = [
    
    path('',home, name="home"),
    path('register/',register, name="register"),
    path('login/<int:pk>/',login_view,name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='templates/logout.html'),name='logout'),

]
