from rest_framework import serializers
from finalProject.shipper.models import Load, ShipperUser

class PriceField(serializers.Field):
    def to_representation(self, object):
        try:
            ShipperUser.objects.get(user_id=self.context['request'].user.id)
            return object
        except:
            return object * 0.95

    def to_internal_value(self, data):
        return data

class LoadSerializer(serializers.HyperlinkedModelSerializer):
    price = PriceField()
    shipper = serializers.SerializerMethodField()
    carrier = serializers.SerializerMethodField()

    class Meta:
        model = Load
        fields = ('id', 'pickup_date', 'ref', 'origin_city', 'destination_city', 'price',
                  'status', 'shipper', 'carrier')

    def get_shipper(self, object):
        return object.shipper.user.get_full_name()

    def get_carrier(self, object):
        try:
            return object.carrier.user.get_full_name()
        except:
            return None

