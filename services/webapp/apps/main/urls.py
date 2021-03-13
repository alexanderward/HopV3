from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from apps.main.views.places import PlacesViewset
from apps.main.views.user_scan import UserScanViewset

router = routers.DefaultRouter()
router.register(r'places', PlacesViewset, basename="places")
router.register(r'user-scans', UserScanViewset, basename="user-scans")

urlpatterns = [
    url(r'^', include(router.urls))
]
