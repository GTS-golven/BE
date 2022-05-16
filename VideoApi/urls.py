from django.urls import path
from . import views

urlpatterns = [
    path('videos/', views.VideoCreate.as_view()),
]