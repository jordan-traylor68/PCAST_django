"""
File: views_api.py
Description: NamedEntities backend endpoint implementation
Author: Yujie
Date: 2024/11/4
"""

from rest_framework import viewsets
from .models import Person, Institution
from .serializers import PersonSerializer
from .serializers import InstitutionSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
