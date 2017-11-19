from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django.http import Http404

from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response

import coreapi

from drf_openapi.utils import view_config
from drf_openapi.views import SchemaView

from .serializers import DataEventSerializer

from dashboard.models import DataPipeline

class DataEventAPI(APIView):

    @view_config(response_serializer=DataEventSerializer)
    def post(self, request, version, format=None):
        """
        Post a DataEvent.
        """
        context = {'request': request}
        serializer = DataEventSerializer(data=request.data, many=False, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class APISchemaView(SchemaView):
    permission_classes = (permissions.IsAuthenticated, )