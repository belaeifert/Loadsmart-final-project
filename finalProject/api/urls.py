from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from finalProject.api import views

app_name = "api"

urlpatterns = [
   path('get-token/', views.get_token, name="get_token"),
   path('carrier/list-available/', views.CarrierAvailableLoads.as_view({'get': 'list'}), name='list_carrier_available'),
   path('carrier/list-accepted/', views.CarrierAcceptedLoads.as_view({'get': 'list'}), name='list_carrier_accepted'),
   path('carrier/list-rejected/', views.CarrierRejectedLoads.as_view({'get': 'list'}), name='list_carrier_rejected'),
   path('carrier/accept-load/<int:pk_load>/', views.CarrierAccept, name='accept_load'),
   path('carrier/reject-load/<int:pk_load>/', views.CarrierReject, name='reject_load'),
   path('carrier/drop-load/<int:pk_load>/', views.CarrierDrop, name='drop_load'),
   path('shipper/list-available/', views.ShipperAvailableLoads.as_view({'get': 'list'}), name='list_shipper_available'),
   path('shipper/list-accepted/', views.ShipperAcceptedLoads.as_view({'get': 'list'}), name="list_shipper_accepted"),
   path('shipper/post-load/', views.ShipperPostLoad, name="post_load"),
   path('documentation/', views.apiDocumentation, name="docs"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
