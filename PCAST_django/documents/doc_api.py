# File: doc_api.py
# Description: Backend endpoint implementation for Documents
# Author: Jordan
# Date: 2024-11-04

from rest_framework import viewsets
from .models import Document
from .serializer import Docs_Serializer

class DocViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = Docs_Serializer


