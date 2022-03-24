from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/user/', views.UserCreate.as_view(), name='user-create'),    
    path('auth/user/<int:pk>', views.UserGet.as_view(), name='user-get'),    
]
