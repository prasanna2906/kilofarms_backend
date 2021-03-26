from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,ListModelMixin
from rest_framework.viewsets import GenericViewSet
from . import models
from . import serializers
from rest_framework.decorators import authentication_classes, permission_classes



class RegViewset(GenericViewSet,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):#ListModelMixin):
    queryset = models.Reg.objects.all()
    serializer_class = serializers.RegSerializer
    
    permission_classes = []
    authentication_classes = []
