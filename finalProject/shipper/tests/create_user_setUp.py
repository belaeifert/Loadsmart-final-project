from finalProject.account.models import User
from finalProject.shipper.models import ShipperUser


def createUser():
    user = User.objects.create(email='shipper@teste.com', first_name='shipper', last_name='teste')
    user.save()

    shipper = ShipperUser.objects.create(user=user)
    shipper.save()

    return user, shipper
