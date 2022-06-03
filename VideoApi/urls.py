from webbrowser import get
from django.urls import path, include
from . import views

urlpatterns = [
    path('api/VideoApi/', views.VideosView.as_view('get'), name='video'),        
]
