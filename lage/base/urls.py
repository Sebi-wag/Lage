from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logoutUser, name="logout"),
    path('update-datum/', views.update_datum, name='update-datum'),
]