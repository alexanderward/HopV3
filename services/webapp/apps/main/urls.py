from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from apps.main.views.places import PlacesViewset

router = routers.DefaultRouter()
router.register(r'places', PlacesViewset, basename="places")

urlpatterns = [
    url(r'^', include(router.urls))
]
