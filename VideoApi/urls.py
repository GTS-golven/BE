from django.urls import path
from . import views

urlpatterns = [
    path('videos/', views.VideoCreate.as_view()),
    path('videos/<int:pk>', views.VideoGet.as_view(), name='Video-get'),    
]