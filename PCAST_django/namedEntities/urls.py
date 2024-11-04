from django.urls import path
from . import views_api

urlpatterns = [

    path('api/person/<int:pk>/', views_api.PersonDetailAPIView.as_view(), name='api-person-detail'),
]