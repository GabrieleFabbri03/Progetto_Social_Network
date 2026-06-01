from django.urls import path
from . import views

urlpatterns = [
    # prima pagina che si apre
    path('', views.FeedView.as_view(), name='feed'),
]