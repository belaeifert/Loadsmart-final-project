from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from finalProject.api import views

urlpatterns = [
    path('loads/', views.LoadList.as_view()),
    path('loads/<int:pk>/', views.LoadDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)