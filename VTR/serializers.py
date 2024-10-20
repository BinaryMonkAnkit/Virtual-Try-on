from rest_framework import serializers
from .models import VTR_model

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VTR_model
        fields = '__all__'
