from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,ListModelMixin
from rest_framework.viewsets import GenericViewSet
from . import models
from . import serializers



class ProductViewset(GenericViewSet,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):#ListModelMixin):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    
class ProductGetViewset(GenericViewSet,ListModelMixin):
    serializer_class = serializers.ProductSerializer 
    def get_queryset(self):
        queryset = models.Product.objects.filter(pk=self.kwargs['pk'])
        return queryset