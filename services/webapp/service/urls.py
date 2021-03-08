from django.conf import settings
from django.conf.urls import url
from django.urls import include

urlpatterns = []

if 'apps.main' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^api/', include('apps.main.urls'))]
