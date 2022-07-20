from rest_framework import serializers
from .models import MyUser

class MyUserSerializer(serializers.ModelSerializer):
    #Validators
    class Meta:
        model = MyUser
        fields = ['id','first_name','last_name','company_name','age','city','state','zip','email','web']