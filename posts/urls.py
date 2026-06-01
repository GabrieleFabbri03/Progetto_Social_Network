from django.urls import path
from . import views

urlpatterns = [
    # prima pagina che si apre
    path('', views.FeedView.as_view(), name='feed'),
    path('post/<int:pk>/modifica/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/cancella/', views.PostDeleteView.as_view(), name='post-delete'),
]