from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include("Auth_user.urls")),
    path('tarefas/',include("Tarefas.urls")),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)