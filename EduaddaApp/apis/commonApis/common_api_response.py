from django.http import JsonResponse
from typing import TypeVar, Generic
from EduaddaApp.constants import *
T = TypeVar('T')

class CbtCommonApiResponse(Generic[T]):
    
    def __init__(self, value: T, status: str, message:str=CbtMessage.SendSuccessMsg, CbtCount:int=0, arrayName:str=CbtArrayName.Common, api_type:str='') -> None:
        self.status = status
        self.value = value
        self.arrayName=arrayName
        self.message=message
        self.CbtCount = CbtCount
        self.api_type = api_type

    def cbtResponse(self)->JsonResponse :
        
        if self.status==ApiStatus.Success:
            data={
                ApiStatus.Status: ApiStatus.Success,
                ApiStatus.Message: self.message,
                'TOTAL_COUNT': self.CbtCount,
                self.arrayName: CbtData(self.value, api_type=self.api_type).cbtResData()
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

    def cbtResData(self) -> T:
        return {
            'ITEM_DATA': IListRes(self.value, api_type=self.api_type).listRes(),
            'LIST_HEADER': IListH(self.value, api_type=self.api_type).listResH(),
            'IS_HEADER': False,
        }
    
class IListRes:
    def __init__(self, value: T, api_type:str='') -> T:
        self.value = value
        self.api_type = api_type

    def listRes(self) -> T:            
        original_list = []

        for i in self.value:
            original_list.append(ItemData(i, api_type=self.api_type).itemRes())

        return original_list

class CbtHeader:

    def __init__(self, title, value, color:str='', bg_color:str='', flex:int=1, is_click:bool=False, font_size:int=14, align_row:str='LEFT', align:str='LEFT', icon:str='', click_url:str=''):
      self.title = title
      self.value = value
      self.color = color
      self.bg_color = bg_color
      self.flex = flex
      self.is_click = is_click
      self.font_size = font_size
      self.align_row = align_row
      self.align = align
      self.icon = icon
      self.click_url = click_url

    def hRes(self)->T:
        data = {
            'TITLE': self.title,
            'VALUE': self.value,
            'COLOR': self.color,
            'BG_COLOR': self.bg_color,
            'FLEX': self.flex,
            'IS_CLICK': self.is_click,
            'ALIGN_ROW': self.align_row,
            'ALIGN': self.align,
            'FONT_SIZE': self.font_size,
            'ICON': self.icon,
            'CLICK_URL': self.click_url
        }
        return data

class IListH:
    def __init__(self, value: T, api_type:str='') -> T:
        self.value = value
        self.api_type = api_type

    def listResH(self) -> T:
            
        original_list = []

        if len(self.value) == 0:
            original_list = []

        elif self.api_type == 'CBT_BANNER':
            original_list.append(CbtCommonDataRes(self.value[0], is_header=True).bannerDataResponse())

        elif self.api_type == 'CBT_MENU':
            original_list.append(CbtCommonDataRes(self.value[0], is_header=True).menuDataResponse())

        elif self.api_type == 'CBT_SUBMENU':
            original_list.append(CbtCommonDataRes(self.value[0], is_header=True).submenuDataResponse())

        elif self.api_type == 'CBT_DEPARTMENT':
            original_list.append(CbtCommonDataRes(self.value[0], is_header=True).departmentDataResponse())

        elif self.api_type == 'CBT_DESIGNATION':
            original_list.append(CbtCommonDataRes(self.value[0], is_header=True).designationDataResponse())

        return original_list

class ItemData(Generic[T]):
    def __init__(self, value: T, api_type:str=''):
        self.value = value
        self.api_type = api_type
    
    def itemRes(self)-> T:
        
        if self.api_type == 'CBT_BANNER':
            data = {
                'ID': self.value['PR_BANNER_ID'],
                'TITLE': self.value['PR_TITLE'],
                'IMAGE': '',
                'SUBTITLE': '',
                'SELECTED': False,
                'IS_EXPANDED': False,
                'ORIGINAL_DATA': self.value,
                'ROW_DATA': CbtCommonDataRes(value=self.value).bannerDataResponse(),
                'EXPANDABLE_DATA': [],
                'BG_COLOR': '',
            }            
            return data

        if self.api_type == 'CBT_MENU':
            data = {
                'ID': self.value['PR_MENU_ID'],
                'TITLE': self.value['PR_NAME'],
                'IMAGE': '',
                'SUBTITLE': '',
                'SELECTED': False,
                'IS_EXPANDED': False,
                'ORIGINAL_DATA': self.value,
                'ROW_DATA': CbtCommonDataRes(value=self.value).menuDataResponse(),
                'EXPANDABLE_DATA': [],
                'BG_COLOR': '',
            }            
            return data
        
        if self.api_type == 'CBT_SUBMENU':
            data = {
                'ID': self.value['PR_SUBMENU_ID'],
                'TITLE': self.value['PR_NAME'],
                'IMAGE': '',
                'SUBTITLE': '',
                'SELECTED': False,
                'IS_EXPANDED': False,
                'ORIGINAL_DATA': self.value,
                'ROW_DATA': CbtCommonDataRes(value=self.value).submenuDataResponse(),
                'EXPANDABLE_DATA': [],
                'BG_COLOR': '',
            }            
            return data

        if self.api_type == 'CBT_DEPARTMENT':
            data = {
                'ID': self.value['PR_DEPARTMENT_ID'],
                'TITLE': self.value['PR_NAME'],
                'IMAGE': '',
                'SUBTITLE': '',
                'SELECTED': False,
                'IS_EXPANDED': False,
                'ORIGINAL_DATA': self.value,
                'ROW_DATA': CbtCommonDataRes(value=self.value).departmentDataResponse(),
                'EXPANDABLE_DATA': [],
                'BG_COLOR': '',
            }            
            return data

        if self.api_type == 'CBT_DESIGNATION':
            data = {
                'ID': self.value['PR_DESIGNATION_ID'],
                'TITLE': self.value['PR_NAME'],
                'IMAGE': '',
                'SUBTITLE': '',
                'SELECTED': False,
                'IS_EXPANDED': False,
                'ORIGINAL_DATA': self.value,
                'ROW_DATA': CbtCommonDataRes(value=self.value).designationDataResponse(),
                'EXPANDABLE_DATA': [],
                'BG_COLOR': '',
            }            
            return data

class CbtCommonDataRes:
    def __init__(self, value: T, is_header=False) -> T:
        self.value = value
        self.is_header = is_header
    
    def bannerDataResponse(self)-> T:
        data = []
        data.append(CbtHeader(title='Id', value=self.value['PR_BANNER_ID'] if self.is_header != True else '').hRes())
        data.append(CbtHeader(title='Title', value=self.value['PR_TITLE'] if self.is_header != True else '').hRes())
        data.append(CbtHeader(title='Status', value=cbtStatusTxt(self.value['PR_STATUS']) if self.is_header != True else '').hRes())
        data.append(CbtHeader(title='Created At', value=self.value['PR_CREATED_AT'] if self.is_header != True else '').hRes())
        
        return data
    
    def menuDataResponse(self)-> T:
        data = []
        data.append(CbtHeader(title='Id', value=self.value['PR_MENU_ID'] if self.is_header != True else '').hRes())
        data.append(CbtHeader(title='Menu Name', value=self.value['PR_NAME'] if self.is_header != True else '').hRes())
        data.append(CbtHeader(title='Status', value=cbtStatusTxt(self.value['PR_STATUS']) if self.is_header != True else '').hRes())
        data.append(CbtHeader(title='Created At', value=self.value['PR_CREATED_AT'] if self.is_header != True else '').hRes())
        
        return data
    
    def submenuDataResponse(self)-> T:
        data = []
        data.append(CbtHeader(title='Id', value=self.value['PR_SUBMENU_ID'] if self.is_header != True else '').hRes())
        data.append(CbtHeader(title='Menu', value=self.value['PR_MENU']['PR_NAME'] if self.is_header != True else '').hRes())
        data.append(CbtHeader(title='Submenu Name', value=self.value['PR_NAME'] if self.is_header != True else '').hRes())
        data.append(CbtHeader(title='Status', value=cbtStatusTxt(self.value['PR_STATUS']) if self.is_header != True else '').hRes())
        data.append(CbtHeader(title='Created At', value=self.value['PR_CREATED_AT'] if self.is_header != True else '').hRes())
        
        return data
    
    def departmentDataResponse(self)-> T:
        data = []
        data.append(CbtHeader(title='Id', value=self.value['PR_DEPARTMENT_ID'] if self.is_header != True else '').hRes())
        data.append(CbtHeader(title='Department Name', value=self.value['PR_NAME'] if self.is_header != True else '').hRes())
        data.append(CbtHeader(title='Status', value=cbtStatusTxt(self.value['PR_STATUS']) if self.is_header != True else '').hRes())
        data.append(CbtHeader(title='Created At', value=self.value['PR_CREATED_AT'] if self.is_header != True else '').hRes())
        
        return data
    
    def designationDataResponse(self)-> T:
        data = []
        data.append(CbtHeader(title='Id', value=self.value['PR_DESIGNATION_ID'] if self.is_header != True else '').hRes())
        data.append(CbtHeader(title='Department', value=self.value['PR_DEPARTMENT']['PR_NAME'] if self.is_header != True else '').hRes())
        data.append(CbtHeader(title='Designation Name', value=self.value['PR_NAME'] if self.is_header != True else '').hRes())
        data.append(CbtHeader(title='Status', value=cbtStatusTxt(self.value['PR_STATUS']) if self.is_header != True else '').hRes())
        data.append(CbtHeader(title='Created At', value=self.value['PR_CREATED_AT'] if self.is_header != True else '').hRes())
        
        return data
    