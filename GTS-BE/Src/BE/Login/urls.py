from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('login/<int:id>/', views.LoginView.as_view(), name='loginById'),
    path('register/', views.UserCreate.as_view(), name='register'),
]