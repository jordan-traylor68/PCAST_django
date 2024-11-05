# File: doc_api.py
# Description: Backend endpoint implementation for Documents
# Author: Jordan
# Date: 2024-11-04

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Document
from .serializer import Docs_Serializer

class DocDetailAPIView(APIView):
    def get(self, request, pk):
        document = get_object_or_404(Document, pk=pk)
        serializer = Docs_Serializer(Document)
        return Response(serializer.data, status=status.HTTP_200_OK)


