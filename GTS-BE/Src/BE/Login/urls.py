from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('login/<int:id>/', views.LoginView.as_view()),
]