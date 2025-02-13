from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from EduaddaApp.models import *


class EduaddaBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EduaddaBanner
        fields = ('__all__')