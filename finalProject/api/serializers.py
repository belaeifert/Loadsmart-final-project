from rest_framework import serializers
from finalProject.api.models import Load


class LoadSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    origin = serializers.CharField(required=False, allow_blank=True, max_length=100)
    status = serializers.CharField(max_length=50)
    destination = serializers.CharField(max_length=100)
    price = serializers.FloatField()

    def create(self, validated_data):
        """
        Create and return a new `Load` instance, given the validated data.
        """
        return Load.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Load` instance, given the validated data.
        """
        instance.origin = validated_data.get('origin', instance.origin)
        instance.status = validated_data.get('status', instance.status)
        instance.destination = validated_data.get('destination', instance.destination)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance