from django.urls import path, include
from . import views

urlpatterns = [
    path('auth/register/', views.UserCreate.as_view(), name='user-create'),    
    path('auth/user/', views.UserGet.as_view(), name='user-get'),    
    path('auth/user/<int:pk>', views.UserEdit.as_view(), name='user-edit'),    
]
