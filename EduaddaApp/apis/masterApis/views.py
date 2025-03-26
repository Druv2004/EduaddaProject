from rest_framework import viewsets
from EduaddaApp.cbt_api_response import CbtApiResponse
from . master_api_response import CbtMasterApiResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from EduaddaApp.constants import *
from . serializers import *
from EduaddaApp.helpers import *
import jwt

from . helpers import *
import re
import uuid
   
# ========== USER API's CLASS HERE ==========
class CbtUserViewSet(viewsets.ModelViewSet):
    
    # USER LIST FUNCTION HERE
    def userList(self, request):
        try:
            data = request.data
            
           
            if data.get('USER_ID') is not None:
                data_obj = EduaddaUser.objects.get(USER_ID=data.get('USER_ID'))
                serializer = EduaddaUserSerializer(data_obj)
            
            else:
                data_objs = EduaddaUser.objects.all()
                serializer = EduaddaUserSerializer(data_objs, many=True)

            return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()

            
   
        except Exception as ex:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()   

    # USER REGISTER FUNCTION HERE
    def userRegister(self, request):
        try:
            data = request.data

            # Check if the email already exists
            if EduaddaUser.objects.filter(EMAIL=data.get('EMAIL')).exists():
                return CbtApiResponse([], ApiStatus.Exist, CbtMessage.existMsg('User email')).cbtResponse()

            # Prepare user data
            user_data = {
                'NAME': data.get('NAME'),
                'EMAIL': data.get('EMAIL'),
                'IS_ACTIVE': 0,
                'PASSWORD': make_password(data.get('PASSWORD')),  # Hash the password
            }

            # Serialize and save the data
            serializer = EduaddaUserSerializer(data=user_data)
            if serializer.is_valid():
                serializer.save()
                return CbtApiResponse([], ApiStatus.Success, CbtMessage.cbtMsg('User has been successfully created!!')).cbtResponse()

            return CbtApiResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()

        except Exception as ex:
            print(f"Exception: {ex}")
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse() 
        
        
    # USER LOGIN FUNCTION HERE
    def userLogin(self, request):
        from datetime import datetime, timedelta
        try:
            data = request.data

            # Validate input
            email = data.get('EMAIL')
            password = data.get('PASSWORD')

            if not email or not password:
                return CbtApiResponse([], ApiStatus.Failure, CbtMessage.cbtMsg("Your login detail isn't valid!!")).cbtResponse()

            try:
                # Retrieve user by email
                user_obj = EduaddaUser.objects.get(EMAIL=email)
            except EduaddaUser.DoesNotExist:
                return CbtApiResponse([], ApiStatus.Failure, CbtMessage.cbtMsg("Your login detail isn't valid!!")).cbtResponse()

            # Check if the password matches
            if not check_password(password, user_obj.PASSWORD):
                return CbtApiResponse([], ApiStatus.Failure, CbtMessage.cbtMsg("Your login detail isn't valid!!")).cbtResponse()

            # Generate a unique token for the session
            token = str(uuid.uuid4())
            expiration_time = datetime.now() + timedelta(hours=24)  # Token expires in 24 hours

            # Create a new session for the user (no need to update IS_ACTIVE here)
            UserSession.objects.create(
                USER=user_obj,
                TOKEN=token,
                DEVICE_INFO=request.META.get('HTTP_USER_AGENT', 'Unknown'),
                IP_ADDRESS=request.META.get('REMOTE_ADDR', ''),
                EXPIRES_AT=expiration_time
            )
            request.session['user_id'] = user_obj.USER_ID
            request.session.save()

            # Set IS_ACTIVE to 1 if the user has at least one active session
            if not UserSession.objects.filter(USER=user_obj).exists():
                user_obj.IS_ACTIVE = 0  # This would mean the user has no active sessions
            else:
                user_obj.IS_ACTIVE = 1
            user_obj.save()

            # Prepare response data
            response_data = {
                "USER_ID": user_obj.USER_ID,
                "TOKEN": token,
                "IS_ACTIVE": user_obj.IS_ACTIVE,
                "EXPIRES_AT": expiration_time
            }

            return CbtApiResponse(response_data, ApiStatus.Success, CbtMessage.LoginSuccessMsg).cbtResponse()

        except Exception as ex:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()





    # USER LOGOUT FUNCTION HERE
    def userLogout(self, request):
        try:
            data = request.data
            
            try:
                user_obj = EduaddaUser.objects.get(USER_ID=data.get('USER_ID'))
            except:
                user_obj = None
            
            if user_obj is None:
                return CbtApiResponse([], ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()
            
        
            EduaddaUser.objects.filter(USER_ID=data.get("USER_ID")).update(IS_ACTIVE=0)
            
            return CbtApiResponse([], ApiStatus.Success, CbtMessage.cbtMsg("Your account has been successfully logout!!")).cbtResponse()
            
            

        except Exception as ex:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()   
      
    # USER PROFILE DATA FUNCTION HERE
    def userProfile(self, request):
        try:
            data = request.data
            
            try:
                user_obj = EduaddaUser.objects.get(USER_ID=data.get('USER_ID'))
            except:
                user_obj = None
            
            if user_obj is None:
                return CbtApiResponse([], ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()
            
            serializer = EduaddaUserSerializer(user_obj)
            return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()
        
            

        except Exception as ex:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()   
      
    # USER PROFILE UPDATE FUNCTION HERE   
    def userProfileUpdate(self, request):
        try:
            data = request.data
            
            try:
                user_obj = EduaddaUser.objects.get(USER_ID=data.get('USER_ID'))
            except:
                user_obj = None
            
            if user_obj is None:
                return CbtApiResponse([], ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()
            
            serializer = EduaddaUserUpdateSerializer(user_obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return CbtApiResponse([], ApiStatus.Success, CbtMessage.UpdateSuccessMsg).cbtResponse()
            
            
            return CbtApiResponse([], ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()
                

        except Exception as ex:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()   
        
    # FORGET PASSWORD FUNCTION HERE
    def forgetPassword(self, request):
        try:
            data = request.data
            print("Email being sent for OTP:", data.get('EMAIL'))
            if sendOtp(data.get('EMAIL')):
                return CbtApiResponse([], ApiStatus.Success, CbtMessage.cbtMsg('Otp has been send on your email address!!')).cbtResponse()

            return CbtApiResponse([], ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()
                
        except Exception as ex:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()   
        
        
          
    # CHANGE PASSWORD FUNCTION HERE
    def changePassword(self, request):
        try:
            data = request.data
            try:
                user_obj = EduaddaUser.objects.get(EMAIL=data.get('EMAIL'))
            except:
                user_obj = None

            if user_obj is None:
                return CbtApiResponse([], ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()

            if user_obj.PR_OTP != data.get('OTP'):
                return CbtApiResponse([], ApiStatus.Failure, CbtMessage.cbtMsg("Your otp isn't valid!!")).cbtResponse()

            old = str(user_obj.PR_OTP_TIME).split('.')[0]
            new = str(datetime.datetime.today()).split('.')[0]
            
            time = datetime.datetime.strptime(new, '%Y-%m-%d %H:%M:%S') - datetime.datetime.strptime(old, '%Y-%m-%d %H:%M:%S')
            
            minutes = time.total_seconds() / 60
            
            if minutes < 16:
                user_password = make_password(data.get('PASSWORD'))
                
                EduaddaUser.objects.filter(USER_ID=user_obj.USER_ID).update(PASSWORD=user_password, )

                return CbtApiResponse([], ApiStatus.Success, CbtMessage.cbtMsg("Your password has been successfully changed!!")).cbtResponse()
            
            return CbtApiResponse([], ApiStatus.Failure, CbtMessage.cbtMsg("Your otp has been expaired!!")).cbtResponse()
    
        except Exception as ex:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()   
        