from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from finalProject.api import views

app_name = "api"

urlpatterns = [
    path('get-token/', views.get_token),
    path('carrier/list-available/', views.CarrierAvailableLoads.as_view({'get': 'list'})),
    path('carrier/list-accepted/', views.CarrierAcceptedLoads.as_view({'get': 'list'})),
    path('carrier/list-rejected/', views.CarrierRejectedLoads.as_view({'get': 'list'})),
    path('carrier/accept-load/<int:pk_load>/', views.CarrierAccept),
    path('carrier/reject-load/<int:pk_load>/', views.CarrierReject),
    path('carrier/drop-load/<int:pk_load>/', views.CarrierDrop),
    path('shipper/list-available/', views.ShipperAvailableLoads.as_view({'get': 'list'})),
    path('shipper/list-accepted/', views.ShipperAcceptedLoads.as_view({'get': 'list'})),
    path('shipper/post-load/', views.ShipperPostLoad),
    path('documentation/', views.apiDocumentation, name="docs"),

]

urlpatterns = format_suffix_patterns(urlpatterns)