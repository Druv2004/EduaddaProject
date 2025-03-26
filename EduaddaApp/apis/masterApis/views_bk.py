from rest_framework import viewsets
from EduaddaApp.cbt_api_response import *
from EduaddaApp.helpers import *
from . serializers import *

# ====== DESIGNATION API's CLASS HERE ======
class CbtDesignationViewSet(viewsets.ModelViewSet):
    
    # Designation add function here
    def designationAdd(self, request):
        try:
            request_data = CbtApiRequestWT(value=request.data).cbtRequest()
            data = request_data.get('CBT_REQUEST_DATA')
            requestActivityData(request_data.get('REQUEST_TRACKING'))
            
            try:
                name = CbtDesignation.objects.get(PR_NAME=data.get('PR_NAME'))
            except:
                name = None

            if name is not None:
                return CbtApiResponse([], ApiStatus.Exist, CbtMessage.existMsg('Name')).cbtResponse()

            serializer = CbtDesignationSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return CbtApiResponse(serializer.data, ApiStatus.Success, CbtMessage.SubmitSuccessMsg).cbtResponse()
            
            return CbtApiResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()
        
        except:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.MessageException).cbtResponse()            

#     # DESIGNATION UPDATE FUNCTION HERE
#     def designationUpdate(self, request):
#         try:
#             request_data = CbtApiRequestWT(value=request.data).cbtRequest()
#             data = request_data.get('CBT_REQUEST_DATA')
#             requestActivityData(request_data.get('REQUEST_TRACKING'))
            
#             data_obj = PrDesignation.objects.get(PR_DESIGNATION_ID=data.get('PR_DESIGNATION_ID'))
#             serializer = PrDesignationSerializer(data_obj, data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return CbtApiResponse(serializer.data, ApiStatus.Success, CbtMessage.UpdateSuccessMsg).cbtResponse()
            
#             return CbtApiResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()
        
#         except:
#             return CbtApiResponse([], ApiStatus.Exception, CbtMessage.MessageException).cbtResponse()            


#     # DESIGNATION DATA LIST FUNCTION HERE
#     def designationList(self, request):
#         try:
#             request_data = CbtApiRequestWT(value=request.data).cbtRequest()
#             data = request_data.get('CBT_REQUEST_DATA')
#             requestActivityData(request_data.get('REQUEST_TRACKING'))
            
#             if data.get('PR_DESIGNATION_ID') is not None:
#                 data_obj = PrDesignation.objects.get(PR_DESIGNATION_ID=data.get('PR_DESIGNATION_ID'))
#                 serializer = PrDesignationDataListSerializer(data_obj)
                
#             else:
#                 data_objs = PrDesignation.objects.all().order_by('-PR_DESIGNATION_ID')
#                 serializer = PrDesignationDataListSerializer(data_objs, many=True)
            
#             return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()
        
#         except:
#             return CbtApiResponse([], ApiStatus.Exception, CbtMessage.MessageException).cbtResponse()


#     # DESIGNATION DATA LIST FUNCTION HERE
#     def designationDataList(self, request):
#         try:
#             request_data = request.data
#             data = request_data.get('CBT_REQUEST_DATA')
#             requestActivityData(request_data.get('REQUEST_TRACKING'))

#             if cbtUserCheck(data.get('USER_ID'), data.get('ORGANIZATION_ID')):

#                 if data.get('PR_DESIGNATION_ID') is not None:
#                     data_obj = PrDesignation.objects.get(PR_DESIGNATION_ID=data.get('PR_DESIGNATION_ID'))
#                     serializer = PrDesignationDataListSerializer(data_obj)
#                     return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()

#                 if data.get('PR_QUERY') != '':
#                     # data_objs = CbtFilterData(data.get('PR_QUERY')).designationData()
#                     data_objs = []
#                 else:
#                     data_objs = PrDesignation.objects.all().order_by('-PR_DESIGNATION_ID')

#                 serializer = PrDesignationDataListSerializer(data_objs, many=True)
                
#                 return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()
#                 # return CbtCommonDataResponse(serializer.data, ApiStatus.Success, api_type='CBT_DESIGNATION_DATA').cbtResponse()

#             return CbtApiResponse([], ApiStatus.Failure, CbtMessage.UserDetailNotValid).cbtResponse()
        
#         except:
#             return CbtApiResponse([], ApiStatus.Exception, CbtMessage.MessageException).cbtResponse()

# # ====== ORGANIZATION API's CLASS HERE ====== 
# class CbtOrgTypeViewSet(viewsets.ModelViewSet):
    
#     # ORGANIZATION TYPE ADD FUNCTION HERE
#     def organizationTypeAdd(self, request):
#         try:
#             request_data = CbtApiRequestWT(value=request.data).cbtRequest()
#             data = request_data.get('CBT_REQUEST_DATA')
#             requestActivityData(request_data.get('REQUEST_TRACKING'))
            
#             try:
#                 name = CbtOrgType.objects.get(PR_NAME=data.get('PR_NAME'))
#             except:
#                 name = None

#             if name is not None:
#                 return CbtApiResponse([], ApiStatus.Exist, CbtMessage.existMsg('Name')).cbtResponse()

#             serializer = CbtOrgTypeSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return CbtApiResponse(serializer.data, ApiStatus.Success, CbtMessage.SubmitSuccessMsg).cbtResponse()

#             return CbtApiResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()
        
#         except:
#             return CbtApiResponse([], ApiStatus.Exception, CbtMessage.MessageException).cbtResponse()            

#     # ORGANIZATION TYPE UPDATE FUNCTION HERE
#     def organizationTypeUpdate(self, request):
#         try:
#             request_data = CbtApiRequestWT(value=request.data).cbtRequest()
#             data = request_data.get('CBT_REQUEST_DATA')
#             requestActivityData(request_data.get('REQUEST_TRACKING'))

#             dept_obj = CbtOrgType.objects.get(PR_ORG_TYPE_ID=data.get('PR_ORG_TYPE_ID'))
#             serializer = CbtOrgTypeSerializer(dept_obj, data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return CbtApiResponse(serializer.data, ApiStatus.Success, CbtMessage.UpdateSuccessMsg).cbtResponse()

#             return CbtApiResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()
        
#         except:
#             return CbtApiResponse([], ApiStatus.Exception, CbtMessage.MessageException).cbtResponse()            
 
#     # ORGANIZATION TYPE LIST FUNCTION HERE
#     def organizationTypeList(self, request):
#         try:
#             request_data = CbtApiRequestWT(value=request.data).cbtRequest()
#             data = request_data.get('CBT_REQUEST_DATA')
#             requestActivityData(request_data.get('REQUEST_TRACKING'))
            
#             if data.get('PR_ORG_TYPE_ID') is not None:
#                 dept_obj = CbtOrgType.objects.get(PR_ORG_TYPE_ID=data.get('PR_ORG_TYPE_ID'))
#                 serializer = CbtOrgTypeDataSerializer(dept_obj)
            
#             else:
#                 dept_objs = CbtOrgType.objects.all()
#                 serializer = CbtOrgTypeDataSerializer(dept_objs, many=True)
            
#             return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()

#         except:
#             return CbtApiResponse([], ApiStatus.Exception, CbtMessage.MessageException).cbtResponse()    

    
#     # ORGANIZATION TYPE DATA LIST FUNCTION HERE
#     def organizationTypeDataList(self, request):
#         try:
#             request_data = request.data
#             data = request_data.get('CBT_REQUEST_DATA')
#             requestActivityData(request_data.get('REQUEST_TRACKING'))

#             if cbtUserCheck(data.get('USER_ID'), data.get('ORGANIZATION_ID')):
            
#                 if data.get('PR_ORG_TYPE_ID') is not None:
#                     data_obj = PrOrganizationType.objects.get(PR_ORG_TYPE_ID=data.get('PR_ORG_TYPE_ID'))
#                     serializer = PrOrganizationTypeSerializer(data_obj)
#                     return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()
                
#                 else:
#                     data_objs = PrOrganizationType.objects.all().order_by('-PR_ORG_TYPE_ID')
#                     serializer = PrOrganizationTypeSerializer(data_objs, many=True)
                    
#                     return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()

#             return CbtApiResponse([], ApiStatus.Failure, CbtMessage.UserDetailNotValid).cbtResponse()

#         except:
#             return CbtApiResponse([], ApiStatus.Exception, CbtMessage.MessageException).cbtResponse()    

# # ====== DEPARTMENT API's CLASS HERE ======
# class PrDepartmentViewSet(viewsets.ModelViewSet):
    
#     # DEPARTMENT ADD FUNCTION HERE
#     def departmentAdd(self, request):
#         try:
#             request_data = CbtApiRequestWT(value=request.data).cbtRequest()
#             data = request_data.get('CBT_REQUEST_DATA')
#             requestActivityData(request_data.get('REQUEST_TRACKING'))

#             try:
#                 name = PrDepartment.objects.get(PR_NAME=data.get('PR_NAME'), PR_ORG_TYPE=data.get('PR_ORG_TYPE'))
#             except:
#                 name = None

#             if name is not None:
#                 return CbtApiResponse([], ApiStatus.Exist, CbtMessage.existMsg(data.get('Name'))).cbtResponse()

#             serializer = PrDepartmentSerializer(data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return CbtApiResponse(serializer.data, ApiStatus.Success, CbtMessage.SubmitSuccessMsg).cbtResponse()

#             return CbtApiResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()
        
#         except:
#             return CbtApiResponse([], ApiStatus.Exception, CbtMessage.MessageException).cbtResponse()            

#     # DEPARTMENT UPDATE FUNCTION HERE
#     def departmentUpdate(self, request):
#         try:
#             request_data = CbtApiRequestWT(value=request.data).cbtRequest()
#             data = request_data.get('CBT_REQUEST_DATA')
#             requestActivityData(request_data.get('REQUEST_TRACKING'))

#             data_obj = PrDepartment.objects.get(PR_DEPARTMENT_ID=data.get('PR_DEPARTMENT_ID'))
#             serializer = PrDepartmentSerializer(data_obj, data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return CbtApiResponse(serializer.data, ApiStatus.Success, CbtMessage.UpdateSuccessMsg).cbtResponse()

#             return CbtApiResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()
        
#         except:
#             return CbtApiResponse([], ApiStatus.Exception, CbtMessage.MessageException).cbtResponse()            
 
#     # DEPARTMENT LIST FUNCTION HERE
#     def departmentList(self, request):
#         try:
#             request_data = CbtApiRequestWT(value=request.data).cbtRequest()
#             data = request_data.get('CBT_REQUEST_DATA')
#             requestActivityData(request_data.get('REQUEST_TRACKING'))
            
#             if data.get('PR_DEPARTMENT_ID') is not None:
#                 dept_obj = PrDepartment.objects.get(PR_DEPARTMENT_ID=data.get('PR_DEPARTMENT_ID'))
#                 serializer = PrDepartmentDataListSerializer(dept_obj)
            
#             else:
#                 dept_objs = PrDepartment.objects.all()
#                 serializer = PrDepartmentDataListSerializer(dept_objs, many=True)
            
#             return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()

#         except:
#             return CbtApiResponse([], ApiStatus.Exception, CbtMessage.MessageException).cbtResponse()    

#     # DEPARTMENT DATA LIST FUNCTION HERE
#     def departmentDataList(self, request):
#         try:
#             request_data = request.data
#             data = request_data.get('CBT_REQUEST_DATA')
#             requestActivityData(request_data.get('REQUEST_TRACKING'))

#             if cbtUserCheck(data.get('USER_ID'), data.get('ORGANIZATION_ID')):
            
#                 if data.get('PR_DEPARTMENT_ID') is not None:
#                     dept_obj = PrDepartment.objects.get(PR_DEPARTMENT_ID=data.get('PR_DEPARTMENT_ID'))
#                     serializer = PrDepartmentDataListSerializer(dept_obj)
#                     return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()
                
#                 if data.get('PR_QUERY') != '':
#                     # data_objs = CbtFilterData(data.get('PR_QUERY')).departmentData()
#                     data_objs = []
#                 else:
#                     data_objs = PrDepartment.objects.all().order_by('-PR_DEPARTMENT_ID')

#                 serializer = PrDepartmentDataListSerializer(data_objs, many=True)
#                 return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()
            
#                 # return CbtCommonDataResponse(serializer.data, ApiStatus.Success, api_type='CBT_DEPARTMENT_DATA').cbtResponse()

#             return CbtApiResponse([], ApiStatus.Failure, CbtMessage.UserDetailNotValid).cbtResponse()

#         except:
#             return CbtApiResponse([], ApiStatus.Exception, CbtMessage.MessageException).cbtResponse()    


# # ====== ORGANIZATION API's CLASS HERE ======
# class PrOrganizationViewSet(viewsets.ModelViewSet):
    
#     # ORGANIZATION ADD FUNCTION HERE
#     def organizationAdd(self, request):
#         try:
#             request_data = CbtApiRequestWT(value=request.data).cbtRequest()
#             data = request_data.get('CBT_REQUEST_DATA')
#             requestActivityData(request_data.get('REQUEST_TRACKING'))
            
#             # ORGANIZATION ADDRESS DATA
#             address_type = request.POST.getlist('PR_ADDRESS_TYPE[]')
#             address = request.POST.getlist('PR_ADDRESS[]')
#             pincode = request.POST.getlist('PR_PINCODE[]')
#             city = request.POST.getlist('PR_CITY[]')
#             state = request.POST.getlist('PR_STATE[]')
#             country = request.POST.getlist('PR_COUNTRY[]')

#             all_address_data = []
#             for i in range(len(address_type)):
#                 address_data = {
#                     'PR_ADDRESS_TYPE': address_type[i],
#                     'PR_ADDRESS': address[i],
#                     'PR_PINCODE': pincode[i],
#                     'PR_CITY': city[i],
#                     'PR_STATE': state[i],
#                     'PR_COUNTRY': country[i]
#                 }
#                 all_address_data.append(address_data) 

#             # DIRECTOR DATA
#             director_name = request.POST.getlist('PR_DIRECTOR_NAME[]')
#             din_no = request.POST.getlist('PR_DIN_NO[]')
#             auth_sign1 = request.POST.getlist('PR_AUTH_SIGN1[]')
#             director_photo = request.POST.getlist('PR_DIRECTOR_PHOTO[]')
            
#             all_director_data = []
#             for j in range(len(director_name)):
#                 director_data = {
#                     'PR_DIRECTOR_NAME': director_name[j],
#                     'PR_DIN_NO': din_no[j],
#                     'PR_AUTH_SIGN1': auth_sign1[j],
#                     'PR_DIRECTOR_PHOTO': director_photo[j] 
#                 }
#                 all_director_data.append(director_data)

#             # AUTHORIZED SIGNATURE DATA
#             role = request.POST.getlist('PR_ROLE[]')
#             template = request.POST.getlist('PR_TEMPLATE[]')
#             signature = request.POST.getlist('PR_AUTH_SIGN2[]')
#             stamp_photo = request.POST.getlist('PR_STAMP_PHOTO[]')

#             all_auth_sign_data = []
#             for k in range(len(role)):
#                 auth_sign_data = {
#                     'PR_ROLE': role[k],
#                     'PR_TEMPLATE': template[k],
#                     'PR_AUTH_SIGN2': signature[k],
#                     'PR_STAMP_PHOTO': stamp_photo[k] 
#                 }
#                 all_auth_sign_data.append(auth_sign_data)
            
#             all_data = {
#                 'PR_ORG_TYPE': request.POST.get('PR_ORG_TYPE'),
#                 'PR_NAME': request.POST.get('PR_NAME'),
#                 'PR_CODE': request.POST.get('PR_CODE'),
#                 'PR_STATE': request.POST.get('PR_STATE'),
#                 'PR_STATE_CODE': request.POST.get('PR_STATE_CODE'),
#                 'PR_CATEGORY': request.POST.get('PR_CATEGORY'),
#                 'PR_CNF_GROUP': request.POST.get('PR_CNF_GROUP'),
#                 'PR_LEDGER_ACCOUNT': request.POST.get('PR_LEDGER_ACCOUNT'),
#                 'PR_LICENCE_NO': request.POST.get('PR_LICENCE_NO'),
#                 'PR_LOGIN_SEQUENCE': request.POST.get('PR_LOGIN_SEQUENCE'),
#                 'PR_NO_OF_ADMIN': request.POST.get('PR_NO_OF_ADMIN'),
#                 'PR_USER_LIMIT': request.POST.get('PR_USER_LIMIT'),
#                 'PR_STATUS': request.POST.get('PR_STATUS'),
#                 'PR_AADHAR_NO': request.POST.get('PR_AADHAR_NO'),
#                 'PR_GST_NO': request.POST.get('PR_GST_NO'),
#                 'PR_CIN_NO': request.POST.get('PR_CIN_NO'),
#                 'PR_PAN_NO': request.POST.get('PR_PAN_NO'),
#                 'PR_DL_NO1': request.POST.get('PR_DL_NO1'),
#                 'PR_DL_NO2': request.POST.get('PR_DL_NO2'),
#                 'PR_TIN_NO': request.POST.get('PR_TIN_NO'),
#                 'PR_FSSAI_NO': request.POST.get('PR_FSSAI_NO'),
#                 'PR_FSSAI_DATE': request.POST.get('PR_FSSAI_DATE'),
#                 'PR_MFG_LICENCE_NO': request.POST.get('PR_MFG_LICENCE_NO'),
#                 'PR_IMPORT_LICENCE_NO': request.POST.get('PR_IMPORT_LICENCE_NO'),
#                 'PR_MEWS_FLASH': request.POST.get('PR_MEWS_FLASH'),
#                 'PR_BANK_NAME': request.POST.get('PR_BANK_NAME'),
#                 'PR_BRANCH_NAME': request.POST.get('PR_BRANCH_NAME'),
#                 'PR_ACCOUNT_NO': request.POST.get('PR_ACCOUNT_NO'),
#                 'PR_IFSC_CODE': request.POST.get('PR_IFSC_CODE'),
#                 'PR_ESI_APPLICABLE_IN_LAST': request.POST.get('PR_ESI_APPLICABLE_IN_LAST'),
#                 'PR_ESI_NO': request.POST.get('PR_ESI_NO'),
#                 'PR_ORGANIZATION_ADDRESS': all_address_data,
#                 'PR_ORGANIZATION_DIRECTOR': all_director_data,
#                 'PR_AUTHORIZED_SIGNATURE': all_auth_sign_data
#             }
            
#             serializer = PrOrganizationDataSerializer(data=all_data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return CbtApiResponse(serializer.data, ApiStatus.Success, CbtMessage.SubmitSuccessMsg).cbtResponse()
            
#             return CbtApiResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid, CbtArrayName.ErrorDetailArray).cbtResponse()
        
#         except:
#             return CbtApiResponse([], ApiStatus.Exception, CbtMessage.MessageException).cbtResponse() 
                
#     #  ORGANIZATION UPDATE FUNCTION HERE 
#     def organizationUpdate(self, request):
#         try:
#             request_data = CbtApiRequestWT(value=request.data).cbtRequest()
#             data = request_data.get('CBT_REQUEST_DATA')
#             requestActivityData(request_data.get('REQUEST_TRACKING'))
            
#             # COMAPNY ADDRESS DATA
#             address_type = request.POST.getlist('PR_ADDRESS_TYPE[]')
#             address = request.POST.getlist('PR_ADDRESS[]')
#             pincode = request.POST.getlist('PR_PINCODE[]')
#             city = request.POST.getlist('PR_CITY[]')
#             state = request.POST.getlist('PR_STATE[]')
#             country = request.POST.getlist('PR_COUNTRY[]')

#             all_address_data = []
#             for i in range(len(address_type)):
#                 address_data = {
#                     'PR_ADDRESS_TYPE': address_type[i],
#                     'PR_ADDRESS': address[i],
#                     'PR_PINCODE': pincode[i],
#                     'PR_CITY': city[i],
#                     'PR_STATE': state[i],
#                     'PR_COUNTRY': country[i]
#                 }
#                 all_address_data.append(address_data) 

#             # DIRECTOR DATA
#             director_name = request.POST.getlist('PR_DIRECTOR_NAME[]')
#             din_no = request.POST.getlist('PR_DIN_NO[]')
#             auth_sign1 = request.POST.getlist('PR_AUTH_SIGN1[]')
#             director_photo = request.POST.getlist('PR_DIRECTOR_PHOTO[]')
            
#             all_director_data = []
#             for j in range(len(director_name)):
#                 director_data = {
#                     'PR_DIRECTOR_NAME': director_name[j],
#                     'PR_DIN_NO': din_no[j],
#                     'PR_AUTH_SIGN1': auth_sign1[j],
#                     'PR_DIRECTOR_PHOTO': director_photo[j] 
#                 }
#                 all_director_data.append(director_data)

#             # AUTHORIZED SIGNATURE DATA
#             role = request.POST.getlist('PR_ROLE[]')
#             template = request.POST.getlist('PR_TEMPLATE[]')
#             signature = request.POST.getlist('PR_AUTH_SIGN2[]')
#             stamp_photo = request.POST.getlist('PR_STAMP_PHOTO[]')

#             all_auth_sign_data = []
#             for k in range(len(role)):
#                 auth_sign_data = {
#                     'PR_ROLE': role[k],
#                     'PR_TEMPLATE': template[k],
#                     'PR_AUTH_SIGN2': signature[k],
#                     'PR_STAMP_PHOTO': stamp_photo[k] 
#                 }
#                 all_auth_sign_data.append(auth_sign_data)
            
#             all_data = {
#                 'PR_ORG_TYPE': request.POST.get('PR_ORG_TYPE'),
#                 'PR_NAME': request.POST.get('PR_NAME'),
#                 'PR_CODE': request.POST.get('PR_CODE'),
#                 'PR_STATE': request.POST.get('PR_STATE'),
#                 'PR_STATE_CODE': request.POST.get('PR_STATE_CODE'),
#                 'PR_CATEGORY': request.POST.get('PR_CATEGORY'),
#                 'PR_CNF_GROUP': request.POST.get('PR_CNF_GROUP'),
#                 'PR_LEDGER_ACCOUNT': request.POST.get('PR_LEDGER_ACCOUNT'),
#                 'PR_LICENCE_NO': request.POST.get('PR_LICENCE_NO'),
#                 'PR_LOGIN_SEQUENCE': request.POST.get('PR_LOGIN_SEQUENCE'),
#                 'PR_NO_OF_ADMIN': request.POST.get('PR_NO_OF_ADMIN'),
#                 'PR_USER_LIMIT': request.POST.get('PR_USER_LIMIT'),
#                 'PR_STATUS': request.POST.get('PR_STATUS'),
#                 'PR_AADHAR_NO': request.POST.get('PR_AADHAR_NO'),
#                 'PR_GST_NO': request.POST.get('PR_GST_NO'),
#                 'PR_CIN_NO': request.POST.get('PR_CIN_NO'),
#                 'PR_PAN_NO': request.POST.get('PR_PAN_NO'),
#                 'PR_DL_NO1': request.POST.get('PR_DL_NO1'),
#                 'PR_DL_NO2': request.POST.get('PR_DL_NO2'),
#                 'PR_TIN_NO': request.POST.get('PR_TIN_NO'),
#                 'PR_FSSAI_NO': request.POST.get('PR_FSSAI_NO'),
#                 'PR_FSSAI_DATE': request.POST.get('PR_FSSAI_DATE'),
#                 'PR_MFG_LICENCE_NO': request.POST.get('PR_MFG_LICENCE_NO'),
#                 'PR_IMPORT_LICENCE_NO': request.POST.get('PR_IMPORT_LICENCE_NO'),
#                 'PR_MEWS_FLASH': request.POST.get('PR_MEWS_FLASH'),
#                 'PR_BANK_NAME': request.POST.get('PR_BANK_NAME'),
#                 'PR_BRANCH_NAME': request.POST.get('PR_BRANCH_NAME'),
#                 'PR_ACCOUNT_NO': request.POST.get('PR_ACCOUNT_NO'),
#                 'PR_IFSC_CODE': request.POST.get('PR_IFSC_CODE'),
#                 'PR_ESI_APPLICABLE_IN_LAST': request.POST.get('PR_ESI_APPLICABLE_IN_LAST'),
#                 'PR_ESI_NO': request.POST.get('PR_ESI_NO'),
#                 'PR_ORGANIZATION_ADDRESS': all_address_data,
#                 'PR_ORGANIZATION_DIRECTOR': all_director_data,
#                 'PR_AUTHORIZED_SIGNATURE': all_auth_sign_data
#             }

#             data_obj = PrOrganization.objects.get(PR_ORGANIZATION_ID=request.POST.get('PR_ORGANIZATION_ID'))
#             serializer = PrOrganizationDataSerializer(data_obj, data=all_data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return CbtApiResponse(serializer.data, ApiStatus.Success, CbtMessage.UpdateSuccessMsg).cbtResponse()
            
#             return CbtApiResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid, CbtArrayName.ErrorDetailArray).cbtResponse()
        
#         except:
#             return CbtApiResponse([],ApiStatus.Exception,CbtMessage.MessageException).cbtResponse() 

#     # ORGANIZATION LIST FUNCTION HERE 
#     def organizationList(self, request):
#         try:
#             request_data = CbtApiRequestWT(value=request.data).cbtRequest()
#             data = request_data.get('CBT_REQUEST_DATA')
#             requestActivityData(request_data.get('REQUEST_TRACKING'))
            
#             if data.get('PR_ORGANIZATION_ID') is not None:
#                 data_data = PrOrganization.objects.get(PR_ORGANIZATION_ID=data.get('PR_ORGANIZATION_ID'))
#                 serializer = PrOrganizationDataListSerializer(data_data)
#             else:
#                 data_data = PrOrganization.objects.all()
#                 serializer = PrOrganizationDataListSerializer(data_data, many=True)
            
#             return CbtApiResponse(serializer.data, ApiStatus.Success, CbtMessage.SendSuccessMsg).cbtResponse()

#         except:
#             return CbtApiResponse([],ApiStatus.Exception,CbtMessage.MessageException).cbtResponse()

#     # COMPANY DATA LIST FUNCTION HERE
#     def companyDataList(self, request):
#         try:
#             request_data = request.data
#             data = request_data.get('CBT_REQUEST_DATA')
#             requestActivityData(request_data.get('REQUEST_TRACKING'))
            
#             if cbtUserCheck(data.get('USER_ID'), data.get('ORGANIZATION_ID')):

#                 if data.get('PR_ORGANIZATION_ID') is not None:
#                     data_obj = PrOrganization.objects.get(data.get('PR_COMPANY_ID'))
#                     serializer = PrOrganizationDataListSerializer(data_obj)
#                     return CbtApiResponse(serializer.data, ApiStatus.Success, CbtMessage.SendSuccessMsg).cbtResponse()
                
#                 else:
#                     if data.get('PR_QUERY') != '':
#                         data_objs = []
#                         # data_objs = CbtFilterData(data.get('PR_QUERY')).companyData()
                        
#                     else:
#                         data_objs = PrOrganization.objects.all().order_by('-PR_ORGANIZATION_ID')
#                         serializer = PrOrganizationDataListSerializer(data_objs, many=True)

#                     return CbtApiResponse(serializer.data, ApiStatus.Success, CbtMessage.SendSuccessMsg).cbtResponse()    
#                     # return CbtCommonDataResponse(serializer.data, ApiStatus.Success, api_type='CBT_COMPANY_DATA').cbtResponse()
                
#             return CbtApiResponse([], ApiStatus.Failure, CbtMessage.UserDetailNotValid).cbtResponse()

#         except:
#             return CbtApiResponse([],ApiStatus.Exception,CbtMessage.MessageException).cbtResponse()

# # ====== HEADQUARTER API's CLASS HERE ======
# class PrHeadquarterViewSet(viewsets.ModelViewSet):
    
#     # HEADQUARTER ADD FUNCTION HERE
#     def headquarterAdd(self, request):
#         try:
#             request_data = CbtApiRequestWT(value=request.data).cbtRequest()
#             data = request_data.get('CBT_REQUEST_DATA')
#             requestActivityData(request_data.get('REQUEST_TRACKING'))
        
#             try:
#                 name = PrHeadquarter.objects.get(PR_HEADQUATER=data.get('PR_NAME'), PR_ORGANIZATION=data.get('PR_ORGANIZATION'))
#                 return CbtApiResponse([], ApiStatus.Exist, CbtMessage.existMsg('Name')).cbtResponse()
        
#             except:
#                 name = None

#             try:
#                 code = PrHeadquarter.objects.get(PR_CODE=data.get('PR_CODE'), PR_ORGANIZATION=data.get('PR_ORGANIZATION'))
#                 return CbtApiResponse([], ApiStatus.Exist, CbtMessage.existMsg('Code')).cbtResponse()
            
#             except:
#                 code = None

#             if name is None and code is None:
#                 serializer = PrHeadquarterSerializer(data=data)            
#                 if serializer.is_valid():
#                     serializer.save()
#                     return CbtApiResponse(serializer.data, ApiStatus.Success, CbtMessage.SubmitSuccessMsg).cbtResponse()
                
#                 return CbtApiResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()
            
#         except:
#             return CbtApiResponse(ApiStatus.Exception,CbtMessage.MessageException).cbtResponse() 

#     # HEADQUARTER UPDATE FUNCTION HERE
#     def headquarterUpdate(self, request):
#         try:
#             request_data = CbtApiRequestWT(value=request.data).cbtRequest()
#             data = request_data.get('CBT_REQUEST_DATA')
#             requestActivityData(request_data.get('REQUEST_TRACKING'))

#             data_obj = PrHeadquarter.objects.get(PR_HEADQUARTER_ID=data.get('PR_HEADQUARTER_ID'))
#             serializer = PrHeadquarterSerializer(data_obj, data=data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return CbtApiResponse(serializer.data, ApiStatus.Success, CbtMessage.UpdateSuccessMsg).cbtResponse()
            
#             return CbtApiResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()
   
#         except:
#             return CbtApiResponse([],ApiStatus.Exception,CbtMessage.MessageException).cbtResponse() 


#     # HEADQUARTER LIST FUNCTION HERE
#     def headquarterList(self, request):
#         try:
#             request_data = CbtApiRequestWT(value=request.data).cbtRequest()
#             data = request_data.get('CBT_REQUEST_DATA')
#             requestActivityData(request_data.get('REQUEST_TRACKING'))

#             if data.get('PR_QEADQUARTER_ID') is not None:
#                 data_obj = PrHeadquarter.objects.get(PR_HEADQUARTER_ID=data.get('PR_HEADQUARTER_ID'))
#                 serializer = PrHeadquarterSerializer(data_obj)
            
#             else:
#                 data_objs = PrHeadquarter.objects.all().order_by('-PR_HEADQUARTER_ID')
#                 serializer = PrHeadquarterSerializer(data_objs, many=True)

#             return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()
            
#         except:
#             return CbtApiResponse([],ApiStatus.Exception,CbtMessage.MessageException).cbtResponse() 

#     # HEADQUARTER DATA LIST FUNCTION HERE
#     def headquarterDataList(self, request):
#         try:
#             request_data = request.data
#             data = request_data.get('CBT_REQUEST_DATA')
#             requestActivityData(request_data.get('REQUEST_TRACKING'))

#             if cbtUserCheck(data.get('USER_ID'), data.get('ORGANIZATION_ID')):

#                 if isAdmin(data.get('USER_ID')):
                    
#                     if data.get('HEADQUARTER_ID') is not None:
#                         data_obj = PrHeadquarter.objects.get(PR_HEADQUARTER_ID=data.get('PR_HEADQUARTER_ID'))
#                         serializer = PrHeadquarterSerializer(data_obj)
                        
#                     else:
#                         if data.get('PR_QUERY') != '':
#                             # data_objs = CbtFilterData(data.get('PR_QUERY')).headQuarterData()
#                             data_objs = []
#                         else:
#                             data_objs = PrHeadquarter.objects.filter(PR_ORGANIZATION=data.get('ORGANIZATION_ID')).order_by('-PR_HEADQUARTER_ID')
                    
#                 else:
#                     data_objs = []

#                 serializer = PrHeadquarterSerializer(data_objs, many=True)
#                 return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()
                
#             return CbtApiResponse([], ApiStatus.Failure, CbtMessage.UserDetailNotValid).cbtResponse()
 
#         except:
#             return CbtApiResponse([],ApiStatus.Exception,CbtMessage.MessageException).cbtResponse() 

