from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    path('videos/', views.LoginView.as_view()),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)