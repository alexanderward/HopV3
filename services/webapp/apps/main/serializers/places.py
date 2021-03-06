from rest_framework import serializers
from apps.main.models.places import Place
from apps.main.serializers.base import BaseSerializer


class PlacesSerializer(BaseSerializer):
    hashKey = serializers.CharField(read_only=True)
    rangeKey = serializers.CharField(read_only=True)
    geoJson = serializers.CharField(read_only=True)
    geohash = serializers.CharField(read_only=True)
    nodeData = serializers.JSONField(read_only=True)

    class Meta:
        model = Place
        fields = ["hashKey", "rangeKey", "geoJson", "geohash", "nodeData"]
