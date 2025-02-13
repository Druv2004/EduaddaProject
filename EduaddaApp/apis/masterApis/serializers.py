from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from EduaddaApp.models import *



class EduaddaUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduaddaUser
        fields = ('__all__')

class EduaddaUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduaddaUser
        fields = ['USER_ID', 'NAME', 'EMAIL','ABOUT_ME']
        

