from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('profile/<str:username>/follow/', views.follow_user, name='follow_user'),
    # URL per Login Registrazione e Logout
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile/<str:username>/ban/', views.ban_user, name='ban_user'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]