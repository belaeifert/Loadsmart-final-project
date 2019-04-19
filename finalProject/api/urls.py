from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from finalProject.api import views


router = routers.DefaultRouter()
router.register(r'loads', views.LoadViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    #path('loads/', views.LoadViewSet.as_view(), name='loads'),
    #path('loads/<int:pk>/', views.LoadDetail.as_view(), name='load_detail'),
]

#urlpatterns = format_suffix_patterns(urlpatterns)