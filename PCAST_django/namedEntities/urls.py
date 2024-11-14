from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import PersonViewSet, InstitutionViewSet

router = DefaultRouter()

router.register(r'persons', PersonViewSet)
router.register(r'institution', InstitutionViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(router.urls)),
]