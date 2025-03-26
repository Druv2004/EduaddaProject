from django.http import JsonResponse
from typing import TypeVar, Generic
from . constants import *
T = TypeVar('T')

class CbtApiResponse(Generic[T]):
    def __init__(self, value: T, status: str, message:str=CbtMessage.SendSuccessMsg, arrayName:str=CbtArrayName.Common) -> None:
        self.status = status
        self.value = value
        self.arrayName=arrayName
        self.message=message

    def cbtResponse(self)->JsonResponse :

        if self.status==ApiStatus.Success:
            data={
                ApiStatus.Status: ApiStatus.Success,
                ApiStatus.Message: self.message,
                self.arrayName: self.value
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
                self.arrayName:[]
            }
            return JsonResponse(data)



