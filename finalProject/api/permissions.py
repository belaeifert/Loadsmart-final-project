from rest_framework.permissions import BasePermission

from finalProject.carrier.models import CarrierUser
from finalProject.shipper.models import ShipperUser


class IsCarrier(BasePermission):
    """
    Allows access only to carrier users.
    """

    def has_permission(self, request, view):
        try:
            carrier = CarrierUser.objects.get(user_id=request.user.id)
            return True
        except:
            return False


class IsShipper(BasePermission):
    """
    Allows access only to shipper users.
    """

    def has_permission(self, request, view):
        try:
            shipper = ShipperUser.objects.get(user_id=request.user.id)
            return True
        except:
            return False
