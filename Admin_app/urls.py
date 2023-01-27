from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, AudiViewSet

app_name = "Admin_app"

router = DefaultRouter()
router.register(r'audi_dist', AudiViewSet, basename="audi_dist")
router.register(r'movie_dist', MovieViewSet, basename="movies_dist")

urlpatterns = [    
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
