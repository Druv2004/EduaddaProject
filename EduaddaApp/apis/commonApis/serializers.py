from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from EduaddaApp.models import *
from EduaddaApp.apis.masterApis.serializers import *



class EduaddaCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduaddaCourse
        fields = ('__all__')
        
        
class EduaddaNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduaddaNotes
        fields = ('__all__')


class EduaddaCoursePurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduaddaCoursePurchase
        fields = ('__all__')
        
class EduaddaCoursePurchaseListSerializer(serializers.ModelSerializer):
    COURSE = EduaddaCourseSerializer()
    USER = EduaddaUserSerializer()
    class Meta:
        model = EduaddaCoursePurchase
        fields = ('__all__')
        
class EduaddaNotesPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduaddaNotesPurchase
        fields = ('__all__')
        
class EduaddaNotesPurchaseListSerializer(serializers.ModelSerializer):
    NOTE = EduaddaNotesSerializer()
    USER = EduaddaUserSerializer()
    class Meta:
        model = EduaddaNotesPurchase
        fields = ('__all__')
        
        
class EduaddaFileDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduaddaFileData
        fields = ('__all__')


        
 