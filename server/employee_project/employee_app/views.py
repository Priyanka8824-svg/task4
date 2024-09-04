from django.shortcuts import render
from .models import Employee
from .serializers import EmpSerializer
from rest_framework import viewsets
from account.authenticate import CustomAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.contrib.auth import get_user_model
User = get_user_model()

import logging
logger = logging.getLogger(__name__)

class EmpViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [CustomAuthentication]
    serializer_class = EmpSerializer
    queryset = Employee.objects.all()

    def perform_create(self, serializer):
        serializer.save()
        logger.info(f"Created object: {serializer.data}")

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        logger.info(f"Listed objects: {response.data}")
        return response
    
    def perform_update(self, serializer):
        serializer.save()
        logger.info(f"Updated object: {serializer.data}")

    def perform_destroy(self, instance):
        logger.info(f"Deleted object: {instance}")
        instance.delete()