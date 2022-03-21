from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... the rest of your URLconf goes here ...

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

STATIC_ROOT = "\Users\lpazk\Documents\GitHub\BE\GTS-BE\Src\BE\Videos\videos"
