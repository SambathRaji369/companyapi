from django.urls import path
from .views import CompanyViewSet

urlpatterns = [
    path('companies/', CompanyViewSet.as_view({'get': 'list', 'post': 'create'}), name='company-list'),
    path('companies/<int:pk>/', CompanyViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='company-detail'),
]
