# File: serializer.py
# Description: Serializers for Documents
# Author: Jordan
# Date: 2024-11-04


from rest_framework import serializers
from .models import Document

class Docs_Serializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = Document
        fields = '__all__'