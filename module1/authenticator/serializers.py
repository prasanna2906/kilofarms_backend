from rest_framework import serializers
from .models import Reg

class RegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reg
        fields = '__all__'



        
