from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from finalProject.api import views

app_name = "api"

urlpatterns = [
    path('token/', views.getToken, name="get_token"),
    path('carrier/loads/available/', views.CarrierAvailableLoads.as_view({'get': 'list'}),
         name='list_carrier_available'),
    path('carrier/loads/accepted/', views.CarrierAcceptedLoads.as_view({'get': 'list'}), name='list_carrier_accepted'),
    path('carrier/loads/rejected/', views.CarrierRejectedLoads.as_view({'get': 'list'}), name='list_carrier_rejected'),
    path('carrier/load/accept/<int:pk_load>/', views.carrierAccept, name='accept_load'),
    path('carrier/load/reject/<int:pk_load>/', views.carrierReject, name='reject_load'),
    path('carrier/load/drop/<int:pk_load>/', views.carrierDrop, name='drop_load'),
    path('shipper/loads/available/', views.ShipperAvailableLoads.as_view({'get': 'list'}),
         name='list_shipper_available'),
    path('shipper/loads/accepted/', views.ShipperAcceptedLoads.as_view({'get': 'list'}), name="list_shipper_accepted"),
    path('shipper/load/post/', views.shipperPostLoad, name="post_load"),
    path('documentation/', views.apiDocumentation, name="docs"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
