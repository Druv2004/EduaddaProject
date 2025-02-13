from rest_framework import viewsets
from EduaddaApp.cbt_api_response import CbtApiResponse
from . website_api_response import CbtWebsiteApiResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from EduaddaApp.constants import *
from . serializers import *
from EduaddaApp.helpers import *
from . helpers import *
import re



# ============== BANNER API's CLASS HERE ================
class EduaddaBannerViewSet(viewsets.ModelViewSet):
    
    # BANNER ADD FUNCTION HERE
    def bannerAdd(self, request):
        try:
            data = request.data
            
        
            if EduaddaBanner.objects.filter(PR_TITLE=data.get('PR_TITLE')).exists():
                return CbtApiResponse([], ApiStatus.Failure, CbtMessage.existMsg('Title')).cbtResponse()

            serializer = EduaddaBannerSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

                return CbtApiResponse(serializer.data, ApiStatus.Success, CbtMessage.SubmitSuccessMsg).cbtResponse()
                
            return CbtApiResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()

            
        except Exception as ex:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()
        
        
    # BANNER UPDATE FUNCTION HERE
    def bannerUpdate(self, request):
        try:
            data = request.data
            
            

            data_obj = EduaddaBanner.objects.get(PR_BANNER_ID=data.get('PR_BANNER_ID'))
            serializer =  EduaddaBannerSerializer(data_obj, data=data)
            if serializer.is_valid():
                serializer.save()

                return CbtApiResponse(serializer.data, ApiStatus.Success, CbtMessage.UpdateSuccessMsg).cbtResponse()
        
            return CbtApiResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()

            
        except Exception as ex:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()
        
    
    #  BANNER LIST FUNCTION HERE
    def bannerList(self, request):
        try:
            data = request.data
            
            if data.get('PR_BANNER_ID') is not None:                  
                data_objs = EduaddaBanner.objects.get(PR_BANNER_ID=data.get('PR_BANNER_ID'))
                serializer = EduaddaBannerSerializer(data_objs)
                return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()
            
            elif data.get('PR_BANNER_ID') is None:
                data_objs = EduaddaBanner.objects.filter(PR_STATUS=1)
                serializer = EduaddaBannerSerializer(data_objs, many=True) 
                return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()
            
            else:
                return CbtApiResponse([], ApiStatus.Failure, CbtMessage.DataNotFound).cbtResponse()

        except Exception as ex:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()    