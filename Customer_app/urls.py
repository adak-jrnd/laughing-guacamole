from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieBookingViewSet, CustomerDetailViewSet

app_name = "Customer_app"

router = DefaultRouter()
router.register(r'ticket_booking', MovieBookingViewSet, basename="customer_booking")
router.register(r'customer', CustomerDetailViewSet, basename="customer_detail")

urlpatterns = [    
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
