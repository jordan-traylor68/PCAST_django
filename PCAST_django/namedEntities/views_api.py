"""
File: views_api.py
Description: NamedEntities backend endpoint implementation
Author: Yujie
Date: 2024/11/4
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Person
from .serializers import PersonSerializer

class PersonDetailAPIView(APIView):
    """
    API view to retrieve a single Person object by ID.
    """
    def get(self, request, pk):
        """
            Handles GET request to fetch details of a Person object based on its primary key (pk).

                Parameters:
                - request: The HTTP request object.
                - pk: Primary key (id) of the Person object to be retrieved.

                Returns:
                - JSON response with Person data if found, otherwise a 404 error.
        """

        # Retrieve the Person object by primary key (pk). If not found, return 404 error.
        person = get_object_or_404(Person, pk=pk)
        # Serialize the Person object to JSON format
        serializer = PersonSerializer(person)
        # Return the serialized data in a JSON response with a status code of 200 (OK)
        return Response(serializer.data, status=status.HTTP_200_OK)