from rest_framework import serializers
from finalProject.shipper.models import Load


class LoadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Load
        fields = ('url','pickup_date', 'ref', 'origin_city', 'destination_city', 'price', 'status', 'carrier', 'shipper')

