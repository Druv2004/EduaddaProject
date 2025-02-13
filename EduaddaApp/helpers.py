import datetime
from django.conf import settings
from django.core.mail import send_mail
from . models import *
import uuid
import random

# PAGINATION FUNCTION HERE
def pagination(page):
    
    limit = 20
    start = 0
    end = limit
    
    if page >= 1:
        for i in range(2, page+1):
            start = end
            end = limit*i

        dt = {
            'start': start,
            'end': end
        }
        return dt     
    else:
       return None

# def isUserAuthenticate(login_data):
#     try:
#         if login_data.get('PR_TOKEN') != '':
#             CbtUser.objects.get(PR_CODE=login_data.get('PR_USER_CODE'), PR_TOKEN=login_data.get('PR_TOKEN'))
#             return True
#         return False
#     except:
#         return False
    
# def tokenUpdate(user_data):
#     try:
#         token = uuid.uuid4()
#         CbtUser.objects.filter(PR_USER_ID=user_data.PR_USER_ID).update(PR_TOKEN=token)
#         return CbtUser.objects.get(PR_USER_ID=user_data.PR_USER_ID)
#     except:
#         return None
    
# def userPermission(user_token, submenu_code=None):
#     if submenu_code is None:
#         try:
#             user_obj = CbtUser.objects.get(PR_TOKEN=user_token)
#             return user_obj, True
        
#         except:
#             return "You aren't valid!!", False
#     else:
#         try:
#             user_obj = CbtUser.objects.get(PR_TOKEN=user_token)
#         except:
#             return "You aren't valid!!", False
        
#         try:
#             submenu_obj = CbtSubmenu.objects.get(PR_CODE=submenu_code)
#         except:
#             return "Link isn't valid!!", False
        
        
#         return "You haven't permission!!", False
    
# def loginDetail(user_obj):
#     try:
#         subject = "User login details"
#         message = f"""
#             Dear {user_obj.PR_NAME},
#             Your account has been successfully created, use below details to login the account:
            
#             Company Name: {user_obj.PR_ORGANIZATION.PR_NAME},
#             Company code: {user_obj.PR_ORGANIZATION.PR_CODE},
#             User id: {user_obj.PR_CODE},
#             Email id: {user_obj.PR_EMAIL},
#             Password: {user_obj.PR_PASSWORD_Hint}

#             WEBSITE URL: http://web.codebright.in/
#         """
#         email = user_obj.PR_EMAIL
#         email_from = settings.EMAIL_HOST_USER
#         recipient_list = [email]
#         send_mail(subject, message, email_from, recipient_list)
    
#         return True
    
#     except:
#         return False
        

def sendOtp(email):
    try:
        # Check if the email exists
        try:
            user_obj = EduaddaUser.objects.get(EMAIL=email)
        except EduaddaUser.DoesNotExist:
            print(f"User with email {email} does not exist.")
            return False
        except Exception as ex:
            print(f"An error occurred while finding user: {ex}")
            return False
        
        otp = random.randint(100000, 999999)
        current_date = datetime.datetime.today()
        
        EduaddaUser.objects.filter(USER_ID=user_obj.USER_ID).update(PR_OTP=otp, PR_OTP_TIME=current_date)
        user_obj = EduaddaUser.objects.get(USER_ID=user_obj.USER_ID)
        
        subject = "Forget your password"
        message = f'''
            Dear {user_obj.NAME},
            Your otp (One time password) is: {user_obj.PR_OTP}

            This is valid for 15 minutes.
        '''
        
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user_obj.EMAIL]
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)
        
        return True
    except Exception as ex:
        print(f"An error occurred while sending OTP: {ex}")
        return False

