from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
      
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'name','mobile_number']
       



