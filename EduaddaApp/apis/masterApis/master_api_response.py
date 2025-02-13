from django.http import JsonResponse
from typing import TypeVar, Generic
from EduaddaApp.constants import *
T = TypeVar('T')

class CbtMasterApiResponse(Generic[T]):
    
    def __init__(self, value: T, status: str, message:str=CbtMessage.SendSuccessMsg, CbtCount:int=0, arrayName:str=CbtArrayName.Common, api_type:str='', generic_value='') -> None:
        self.status = status
        self.value = value
        self.arrayName=arrayName
        self.message=message
        self.CbtCount = CbtCount
        self.api_type = api_type
        self.generic_value = generic_value

    def cbtResponse(self)->JsonResponse :
        
        if self.status==ApiStatus.Success:
            data={
                ApiStatus.Status: ApiStatus.Success,
                ApiStatus.Message: self.message,
                'TOTAL_COUNT': self.CbtCount,
                self.arrayName: CbtData(self.value, api_type=self.api_type).cbtResData(self.generic_value)
            }
            return JsonResponse(data)

        elif self.status==ApiStatus.Exception:
            data={
                ApiStatus.Status:ApiStatus.Exception,
                ApiStatus.Message:self.message,
                self.arrayName:[]
            }
            return JsonResponse(data)

        elif self.status==ApiStatus.Permission:
            data={
                ApiStatus.Status:ApiStatus.Permission,
                ApiStatus.Message:self.message,
                self.arrayName:[]
            }
            return JsonResponse(data)

        elif self.status==ApiStatus.Exist:
            data={
                ApiStatus.Status:ApiStatus.Exist,
                ApiStatus.Message:self.message,
                self.arrayName:[]
            }
            return JsonResponse(data)
            
        else :
            data={
                ApiStatus.Status:ApiStatus.Failure,
                ApiStatus.Message:self.message,
                self.arrayName:self.value
            }
            return JsonResponse(data)

class CbtData(Generic[T]):
    def __init__(self, value: T, api_type:str='') -> T:
        self.value = value
        self.api_type = api_type

    def cbtResData(self, generic_value='') -> T:
        return {
            'ITEM_DATA': IListRes(self.value, api_type=self.api_type).listRes(generic_value),
            'LIST_HEADER': IListH(self.value, api_type=self.api_type).listResH(),
            'IS_HEADER': False,
        }
    
class IListRes:
    def __init__(self, value: T, api_type:str='') -> T:
        self.value = value
        self.api_type = api_type

    def listRes(self, generic_value='') -> T:            
        original_list = []

        for i in self.value:
            original_list.append(ItemData(i, api_type=self.api_type).itemRes(generic_value))

        return original_list

# class CbtHeader:
#     def __init__(self, title, value, color:str='', bg_color:str='', flex:int=1, is_click:bool=False, font_size:int=14, align_row:str='LEFT', align:str='LEFT', icon:str='', click_url:str='', click_type_method='POST', request_key='', request_value='', click_type='', btn_click_type=BtnClickType.native, btn_type=BtnType.view):
#         self.title = title
#         self.value = value
#         self.color = color
#         self.bg_color = bg_color
#         self.flex = flex
#         self.is_click = is_click
#         self.font_size = font_size
#         self.align_row = align_row
#         self.align = align
#         self.icon = icon
#         self.click_url = click_url
#         self.click_type_method = click_type_method
#         self.request_key = request_key
#         self.request_value = request_value
#         self.click_type = click_type
#         self.btn_click_type = btn_click_type
#         self.btn_type = btn_type

#     def hRes(self)->T:
#         data = {
#             'TITLE': self.title,
#             'VALUE': self.value,
#             'COLOR': self.color,
#             'BG_COLOR': self.bg_color,
#             'FLEX': self.flex,
#             'IS_CLICK': self.is_click,
#             'ALIGN_ROW': self.align_row,
#             'ALIGN': self.align,
#             'FONT_SIZE': self.font_size,
#             'ICON': self.icon,
#             'CLICK_URL': self.click_url,
#             'CLICK_TYPE_METHOD': self.click_type_method,
#             'REQUEST_KEY': self.request_key,
#             'REQUEST_VALUE': self.request_value,
#             'CLICK_TYPE': self.click_type,
#             'BTN_CLICK_TYPE': self.btn_click_type,
#             "BTN_TYPE": self.btn_type
#         }
#         return data
    
class IListH:
    def __init__(self, value: T, api_type:str='') -> T:
        self.value = value
        self.api_type = api_type

    def listResH(self) -> T:
            
        original_list = []

        if len(self.value) == 0:
            original_list = []
        
        elif self.api_type == 'CBT_ORGANIZATION_DATA':
            original_list.append(CbtMasterDataRes(self.value[0], is_header=True).organizationDataResponse())
        
        elif self.api_type == 'CBT_HEADQUARTER_DATA':
            original_list.append(CbtMasterDataRes(self.value[0], is_header=True).headquarterDataResponse())

        elif self.api_type == 'CBT_USER_DATA':
            original_list.append(CbtMasterDataRes(self.value[0], is_header=True).userDataResponse())
        
        elif self.api_type == 'CBT_ORGANIZATION_PERMISSION_DATA':
            original_list.append(CbtMasterDataRes(self.value[0], is_header=True).organizationPermissionDataResponse())
        
        elif self.api_type == 'CBT_DEPARTMENT_PERMISSION_DATA':
            original_list.append(CbtMasterDataRes(self.value[0], is_header=True).departmentPermissionDataResponse())
        
        elif self.api_type == 'CBT_DESIGNATION_PERMISSION_DATA':
            original_list.append(CbtMasterDataRes(self.value[0], is_header=True).designationPermissionDataResponse())
        
        elif self.api_type == 'CBT_PROJECT_DATA':
            original_list.append(CbtMasterDataRes(self.value[0], is_header=True).projectDataResponse())

        elif self.api_type == 'CBT_MODULE_DATA':
            original_list.append(CbtMasterDataRes(self.value[0], is_header=True).moduleDataResponse())

        return original_list

class ItemData(Generic[T]):
    def __init__(self, value: T, api_type:str=''):
        self.value = value
        self.api_type = api_type
    
    def itemRes(self, generic_value='')-> T:
        
        if self.api_type == 'CBT_ORGANIZATION_DATA':
            data = {
                'ID': self.value['PR_ORGANIZATION_ID'],
                'TITLE': self.value['PR_NAME'],
                'IMAGE': '',
                'SUBTITLE': '',
                'SELECTED': False,
                'IS_EXPANDED': False,
                'DATA': self.value,
                'ROW_DATA': CbtMasterDataRes(value=self.value).organizationDataResponse(),
                'EXPANDABLE_DATA': [],
                'BG_COLOR': '',
            }            
            return data
        
        if self.api_type == 'CBT_HEADQUARTER_DATA':
            data = {
                'ID': self.value['PR_HEADQUATER_ID'],
                'TITLE': self.value['PR_NAME'],
                'IMAGE': '',
                'SUBTITLE': '',
                'SELECTED': False,
                'IS_EXPANDED': False,
                'PERSONAL_DATA': self.value,
                'ROW_DATA': CbtMasterDataRes(value=self.value).headquarterDataResponse(),
                'EXPANDABLE_DATA': [],
                'BG_COLOR': '',
            }            
            return data
        
        if self.api_type == 'CBT_USER_DATA':
            data = {
                'ID': self.value['PR_USER_ID'],
                'TITLE': self.value['PR_NAME'],
                'IMAGE': '',
                'SUBTITLE': '',
                'SELECTED': False,
                'IS_EXPANDED': False,
                'DATA': self.value,
                'ROW_DATA': CbtMasterDataRes(value=self.value).userDataResponse(),
                'EXPANDABLE_DATA': [],
                'BG_COLOR': '',
            }            
            return data
        
        if self.api_type == 'CBT_ORGANIZATION_PERMISSION_DATA':
            data = {
                'ID': self.value['PR_ORGANIZATION_ID'],
                'TITLE': self.value['PR_NAME'],
                'IMAGE': '',
                'SUBTITLE': '',
                'SELECTED': False,
                'IS_EXPANDED': False,
                'DATA': self.value,
                'ROW_DATA': CbtMasterDataRes(value=self.value).organizationPermissionDataResponse(),
                'EXPANDABLE_DATA': [],
                'BG_COLOR': '',
            }            
            return data
        
        if self.api_type == 'CBT_DEPARTMENT_PERMISSION_DATA':
            data = {
                'ID': self.value['PR_DEPARTMENT_ID'],
                'TITLE': self.value['PR_NAME'],
                'IMAGE': '',
                'SUBTITLE': '',
                'SELECTED': False,
                'IS_EXPANDED': False,
                'DATA': self.value,
                'ROW_DATA': CbtMasterDataRes(value=self.value).departmentPermissionDataResponse(),
                'EXPANDABLE_DATA': [],
                'BG_COLOR': '',
            }            
            return data
        
        if self.api_type == 'CBT_DESIGNATION_PERMISSION_DATA':
            data = {
                'ID': self.value['PR_DESIGNATION_ID'],
                'TITLE': self.value['PR_NAME'],
                'IMAGE': '',
                'SUBTITLE': '',
                'SELECTED': False,
                'IS_EXPANDED': False,
                'DATA': self.value,
                'ROW_DATA': CbtMasterDataRes(value=self.value).designationPermissionDataResponse(generic_value),
                'EXPANDABLE_DATA': [],
                'BG_COLOR': '',
            }            
            return data
        
        if self.api_type == 'CBT_PROJECT_DATA':
            data = {
                'ID': self.value['PR_PROJECT_ID'],
                'TITLE': self.value['PR_NAME'],
                'IMAGE': '',
                'SUBTITLE': '',
                'SELECTED': False,
                'IS_EXPANDED': False,
                'DATA': self.value,
                'ROW_DATA': CbtMasterDataRes(value=self.value).projectDataResponse(),
                'EXPANDABLE_DATA': [],
                'BG_COLOR': '',
            }            
            return data
        if self.api_type == 'CBT_MODULE_DATA':
            data = {
                'ID': self.value['PR_MODULE_ID'],
                'TITLE': self.value['PR_NAME'],
                'IMAGE': '',
                'SUBTITLE': '',
                'SELECTED': False,
                'IS_EXPANDED': False,
                'DATA': self.value,
                'ROW_DATA': CbtMasterDataRes(value=self.value).moduleDataResponse(),
                'EXPANDABLE_DATA': [],
                'BG_COLOR': '',
            }            
            return data
               
class CbtMasterDataRes:
    def __init__(self, value: T, is_header=False) -> T:
        self.value = value
        self.is_header = is_header

    