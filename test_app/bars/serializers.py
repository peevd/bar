from .models import Bar
from rest_framework import serializers


class BarSerializer(serializers.HyperlinkedModelSerializer):
    """
    Bar serializer
    """
    class Meta:
        model = Bar
        fields = ("id", "name", "rating", )
        read_only_fields = ("id", "url", "created_at", "updated_at", )
        required_fields = ("name", "rating", )
        extra_kwargs = {field: {"required": True} for field in required_fields}
