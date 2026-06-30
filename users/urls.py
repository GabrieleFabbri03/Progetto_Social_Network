from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Messo qui, Django lo intercetta subito prima di confonderlo con un username
    path('edit/', views.ProfileUpdateView.as_view(), name='edit_profile'),

    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('profile/<str:username>/follow/', views.follow_user, name='follow_user'),
    path('profile/<str:username>/ban/', views.ban_user, name='ban_user'),

    path('<str:username>/', views.profile_view, name='profile'),
]