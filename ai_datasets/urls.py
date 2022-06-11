from django.urls import path
from . import views

urlpatterns = [
    path('ai', views.DataSetVideoView.as_view(), name='DatasetVideo'),
    ]