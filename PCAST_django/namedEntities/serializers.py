"""
File: serializers.py
Description: This file defines serializers for the models in NamedEntities, which are responsible for
             converting model instances to JSON format for use in API responses, and for
             converting JSON data into model instances for saving to the database.
Author: Yujie
Date: 2024/11/4
"""


from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'