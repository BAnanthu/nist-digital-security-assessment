from rest_framework import serializers, status
from rest_framework.serializers import Serializer

from function.models import Identify


class IdentifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Identify
        fields = ['identify_id', 'category_id']

    def create(self, validated_data):
        return Identify.objects.create(**validated_data)

