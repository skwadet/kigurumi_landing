from django.contrib import admin
from django.urls import path
from scumapp.views import *
from scumapp.models import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', index)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
