from rest_framework import serializers

from apps.main.models.user_scan import UserScan
from apps.main.serializers.places import PlacesSerializer


class UserScanSerializer(PlacesSerializer):
    hashKey = serializers.CharField(read_only=True)
    rangeKey = serializers.CharField(read_only=True)
    geoJson = serializers.CharField(read_only=True)
    geohash = serializers.CharField(read_only=True)
    nodeData = serializers.JSONField(read_only=True)

    class Meta:
        model = UserScan
        fields = ["hashKey", "rangeKey", "geoJson", "geohash", "nodeData"]
