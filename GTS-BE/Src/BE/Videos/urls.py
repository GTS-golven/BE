from django.conf import settings
from django.conf.urls import url 
from. import views

#from django.contrib import admin
from django.urls import path, include

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import include, re_path
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet

router = DefaultRouter()
router.register(company, CompanyViewSet, base_name='company')

urlpatterns = [
    re_path('^', include(router.urls)),
]

urlpatterns = [
    path('', views.index)

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns = [
    path('', views.upload_display_video, name='upload_display_video'),
    path('', include('Videos.urls')),
]

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include('Videos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)