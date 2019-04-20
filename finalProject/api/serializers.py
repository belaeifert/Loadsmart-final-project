from rest_framework import serializers
from finalProject.shipper.models import Load


class LoadSerializerForCarrier(serializers.HyperlinkedModelSerializer):
    shipper_name = serializers.SerializerMethodField()
    carrier_price = serializers.SerializerMethodField()

    @classmethod
    def get_shipper_name(self, object):
        return object.shipper.user.get_full_name()
    
    @classmethod
    def get_carrier_price(self, object):
        return object.carrier_price()

    class Meta:
        model = Load
        fields = ('id', 'pickup_date', 'ref', 'origin_city', 'destination_city', 
            'status', 'shipper_name', 'carrier_price')


class LoadSerializerForShipper(serializers.HyperlinkedModelSerializer):
    carrier_name = serializers.SerializerMethodField()

    @classmethod
    def get_carrier_name(self, object):
        return object.carrier.user.get_full_name()

    class Meta:
        model = Load
        fields = ('id', 'pickup_date', 'ref', 'origin_city', 'destination_city', 
            'status', 'carrier_name', 'price')