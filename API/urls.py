from django.urls import path
from API import views

urlpatterns = [
    path('video/', views.video_list),
    path('video/<int:pk>/', views.video_detail),
]

