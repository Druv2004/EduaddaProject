from EduaddaApp.models import *
from . serializers import EduaddaUserSerializer
from hashlib import md5
import random
from django.db.models import Q

# class CbtAccount:
#     def __init__(self, user_data) -> None:
#         self.user_data = user_data
        
#     def userCreate(self):
#         serializer = CbtUserSerializer(data=self.user_data)
#         if serializer.is_valid():
#             serializer.save()
#             user_obj = CbtUser.objects.get(PR_USER_ID=serializer.data['PR_USER_ID'])
            
#             name = user_obj.PR_NAME[0:3]
#             user_code =  name+str(random.randint(1000,9999))
#             user_password = name+str(random.randint(100000,999999))

#             result = md5(user_password.encode())
#             password = result.hexdigest()

#             CbtUser.objects.filter(PR_USER_ID=user_obj.PR_USER_ID).update(PR_CODE=user_code, PR_PASSWORD=password, PR_PASSWORD_Hint=user_password)

#             obj = CbtUser.objects.get(PR_USER_ID=user_obj.PR_USER_ID)
            
#             return obj
#         print(str(serializer.errors))
#         return None
        


class CbtFliterData:

    def _init_(self, query_data) -> None:
        self.query_data = query_data
    
   