from django.urls import path
from API import views
from django.conf.urls import include
# re_path
from rest_framework.routers import DefaultRouter
from API.models import video
from .views import APIViewSet

urlpatterns = [
    path('video/', views.video_list),
    path('video/<int:pk>/', views.video_detail),
    # path('^', include(router.urls)),
]

router = DefaultRouter()
router.register(video, APIViewSet, 
# base_name='router'
)
