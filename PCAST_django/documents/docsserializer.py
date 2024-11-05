from rest_framework import serializers
from documents.models import *

class Docs_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = 