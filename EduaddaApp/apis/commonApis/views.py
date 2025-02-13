import razorpay
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from EduaddaApp.cbt_api_response import CbtApiResponse
from rest_framework import status
from . common_api_response import CbtCommonApiResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from EduaddaApp.constants import *
from . serializers import *
from EduaddaApp.helpers import *
from . helpers import *
import re



# Initialize Razorpay client
client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

@api_view(['POST'])
def create_razorpay_order(request):
    if request.method == 'POST':
        try:
            # Get course ID from the request
            course_id = request.data.get('course_id')
            course = EduaddaCourse.objects.get(COURSE_ID=course_id)
            amount = int(course.PRICE * 100)  # Convert to paise (Razorpay expects amount in paise)

            # Create a Razorpay order
            order = client.order.create({
                'amount': amount,
                'currency': 'INR',
                'payment_capture': 1  # Auto-capture payment
            })

            # Return the order ID to the frontend
            return Response({
                'order_id': order['id'],
                'amount': amount,
                'currency': 'INR',
                'key': settings.RAZORPAY_API_KEY
            })

        except Exception as e:
            return Response({'error': str(e)}, status=400)

    return Response({'error': 'Invalid request method'}, status=405)



@api_view(['POST'])
def create_razorpay_order_notes(request):
    if request.method == 'POST':
        try:
            # Get notes ID from the request
            notes_id = request.data.get('notes_id')
            notes = EduaddaNotes.objects.get(NOTES_ID=notes_id)
            amount = int(notes.PRICE * 100)  # Convert to paise (Razorpay expects amount in paise)

            # Create a Razorpay order
            order = client.order.create({
                'amount': amount,
                'currency': 'INR',
                'payment_capture': 1  # Auto-capture payment
            })

            # Return the order ID to the frontend
            return Response({
                'order_id': order['id'],
                'amount': amount,
                'currency': 'INR',
                'key': settings.RAZORPAY_API_KEY
            })

        except EduaddaNotes.DoesNotExist:
            return Response({'error': 'Notes not found'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=400)

    return Response({'error': 'Invalid request method'}, status=405)
 
# ========= FILE UPLOAD API's CLASS HERE ========
class EduaddaFileDataViewSet(viewsets.ModelViewSet):
    
    # FILE DATA UPLOAD FUNCTION HERE
    def fileDataUpload(self, request):
        try:
            data = request.data
            
            serializer = EduaddaFileDataSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()
            
            return CbtApiResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()
            
        
        except Exception as ex:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()   
        
        
# =============== COURSE DATA API's CLASS HERE ==============
class EduaddaCourseDataViewSet(viewsets.ModelViewSet):
    
    # COURSE DATA ADD FUNCTION HERE 
    def courseAdd(self, request):
        try:
            data = request.data
            
            name = data.get("NAME")
            thumbnail = data.get("THUMBNAIL")
            video = data.get("VIDEO")
            price = data.get("PRICE")
            status = data.get("STATUS")
            category = data.get("CATEGORY")
            
            if not all([name, thumbnail, video, price]):
                missing_fields = [
                    field for field, value in [("NAME", name), ("THUMBNAIL", thumbnail), ("VIDEO", video), ("PRICE", price),("STATUS", status),("CATEGORY", category)]
                    if not value
                ]
                return CbtApiResponse(
                    [],
                    ApiStatus.Failure,
                    CbtMessage.cbtMsg(f"Missing or empty fields: {', '.join(missing_fields)}")
                ).cbtResponse()
            
           
            if EduaddaCourse.objects.filter(NAME=data.get('NAME')).exists():
                return CbtApiResponse([], ApiStatus.Failure, CbtMessage.existMsg('Course')).cbtResponse()
            
            serializer = EduaddaCourseSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

                return CbtApiResponse(serializer.data, ApiStatus.Success, CbtMessage.SubmitSuccessMsg).cbtResponse()                  
            return CbtApiResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()

                
        except Exception as ex:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()   
      
    # COURSE DATA UPDATE FUNCTION HERE 
    def courseUpdate(self, request):
        try:
            data = request.data
            
            name = data.get("NAME")
            thumbnail = data.get("THUMBNAIL")
            video = data.get("VIDEO")
            price = data.get("PRICE")
            status = data.get("STATUS")
            category = data.get("CATEGORY")
            
            if not all([name, thumbnail, video, price]):
                missing_fields = [
                    field for field, value in [("NAME", name), ("THUMBNAIL", thumbnail), ("VIDEO", video), ("PRICE", price),("STATUS", status),("CATEGORY", category)]
                    if not value
                ]
                return CbtApiResponse(
                    [],
                    ApiStatus.Failure,
                    CbtMessage.cbtMsg(f"Missing or empty fields: {', '.join(missing_fields)}")
                ).cbtResponse()
            
            
            data_obj = EduaddaCourse.objects.get(COURSE_ID=data.get('COURSE_ID'))    
            serializer = EduaddaCourseSerializer(data_obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return CbtApiResponse(serializer.data, ApiStatus.Success, CbtMessage.UpdateSuccessMsg).cbtResponse()
                
            return CbtApiResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()

                
        except Exception as ex:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()   

    #  COURSE LIST FUNCTION HERE
    def courseList(self, request):
        try:
            data = request.data
            

            if data.get('COURSE_ID') is not None:                  
                data_objs = EduaddaCourse.objects.get(COURSE_ID=data.get('COURSE_ID'))
                serializer = EduaddaCourseSerializer(data_objs)
                return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()
            
            else:
                data_objs = EduaddaCourse.objects.filter(STATUS = 1)
                serializer = EduaddaCourseSerializer(data_objs, many=True)
                return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()
            
            
        except Exception as ex:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse() 



    # =============== NOTES DATA API's CLASS HERE ==============
class EduaddaNotesDataViewSet(viewsets.ModelViewSet):
    
    # NOTES DATA ADD FUNCTION HERE 
    def notesAdd(self, request):
        try:
            data = request.data
            
            name = data.get("NAME")
            thumbnail = data.get("THUMBNAIL")
            pdf = data.get("PDF")
            price = data.get("PRICE")
            status = data.get("STATUS")
            category = data.get("CATEGORY")
            
            if not all([name, thumbnail, price, pdf]):
                missing_fields = [
                    field for field, value in [("NAME", name), ("THUMBNAIL", thumbnail),("PDF", pdf), ("PRICE", price),("STATUS", status),("CATEGORY", category)]
                    if not value
                ]
                return CbtApiResponse(
                    [],
                    ApiStatus.Failure,
                    CbtMessage.cbtMsg(f"Missing or empty fields: {', '.join(missing_fields)}")
                ).cbtResponse()
            
           
            if EduaddaNotes.objects.filter(NAME=data.get('NAME')).exists():
                return CbtApiResponse([], ApiStatus.Failure, CbtMessage.existMsg('Notes')).cbtResponse()
            
            serializer = EduaddaNotesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

                return CbtApiResponse(serializer.data, ApiStatus.Success, CbtMessage.SubmitSuccessMsg).cbtResponse()                  
            return CbtApiResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()

                
        except Exception as ex:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()   
      
    # NOTES DATA UPDATE FUNCTION HERE 
    def notesUpdate(self, request):
        try:
            data = request.data
            
            name = data.get("NAME")
            thumbnail = data.get("THUMBNAIL")
            pdf = data.get("PDF")
            price = data.get("PRICE")
            status = data.get("STATUS")
            category = data.get("CATEGORY")
            
            if not all([name, thumbnail, price]):
                missing_fields = [
                    field for field, value in [("NAME", name), ("THUMBNAIL", thumbnail),("PDF", pdf), ("PRICE", price),("STATUS", status),("CATEGORY", category)]
                    if not value
                ]
                return CbtApiResponse(
                    [],
                    ApiStatus.Failure,
                    CbtMessage.cbtMsg(f"Missing or empty fields: {', '.join(missing_fields)}")
                ).cbtResponse()
            
            
            data_obj = EduaddaNotes.objects.get(NOTES_ID=data.get('NOTES_ID'))    
            serializer = EduaddaNotesSerializer(data_obj, data=data)
            if serializer.is_valid():
                serializer.save()
                return CbtApiResponse(serializer.data, ApiStatus.Success, CbtMessage.UpdateSuccessMsg).cbtResponse()
                
            return CbtApiResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()

                
        except Exception as ex:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()   

    #  NOTES LIST FUNCTION HERE
    def notesList(self, request):
        try:
            data = request.data
            

            if data.get('NOTES_ID') is not None:                  
                data_objs = EduaddaNotes.objects.get(NOTES_ID=data.get('NOTES_ID'))
                serializer = EduaddaNotesSerializer(data_objs)
                return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()
            
            else:
                data_objs = EduaddaNotes.objects.filter(STATUS= 1)
                serializer = EduaddaNotesSerializer(data_objs, many=True)
                return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()
            
            
        except Exception as ex:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse() 

    
    
    
# =============== COURSE PURCHASE DATA API's CLASS HERE ==============
class EduaddaCoursePurchaseDataViewSet(viewsets.ModelViewSet):
    def purchaseCourse(self, request):     
        try:
            data = request.data
            
            try:
                name = EduaddaCoursePurchase.objects.get(USER=data.get('USER'), COURSE=data.get('COURSE'))
            except:
                name = None
            
            if name is not None:
                return CbtApiResponse([], ApiStatus.Exist, CbtMessage.existMsg('Course')).cbtResponse()
            
            
            serializer = EduaddaCoursePurchaseSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return CbtApiResponse(serializer.data, ApiStatus.Success, CbtMessage.PurchaseSuccessMsg).cbtResponse()

            return CbtApiResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()


        except Exception as ex:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse() 
        
        
        
    def purchaseCourseList(self, request):
        try:
            data = request.data
            

            if data.get('USER') is not None:                  
                data_objs = EduaddaCoursePurchase.objects.filter(USER=data.get('USER'))
                serializer = EduaddaCoursePurchaseListSerializer(data_objs, many=True)
                return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()
            
            else:
                data_objs = EduaddaCoursePurchase.objects.all()
                serializer = EduaddaCoursePurchaseListSerializer(data_objs, many=True)
                return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()
               
            
        except Exception as ex:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse() 
            



# =============== NOTES PURCHASE DATA API's CLASS HERE ==============
class EduaddaNotesPurchaseDataViewSet(viewsets.ModelViewSet):
    def purchaseNotes(self, request):
        try:
            data = request.data
            
            try:
                name = EduaddaNotesPurchase.objects.get(USER=data.get('USER'), NOTE=data.get('NOTE'))
            except:
                name = None
            
            if name is not None:
                return CbtApiResponse([], ApiStatus.Exist, CbtMessage.existMsg('Notes')).cbtResponse()
            
            
            serializer = EduaddaNotesPurchaseSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return CbtApiResponse(serializer.data, ApiStatus.Success, CbtMessage.PurchaseSuccessMsg).cbtResponse()

            return CbtApiResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()


        except Exception as ex:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse() 
        
        
    def purchaseNotesList(self, request):
        try:
            data = request.data
            

            if data.get('USER') is not None:                  
                data_objs = EduaddaNotesPurchase.objects.filter(USER=data.get('USER'))
                serializer = EduaddaNotesPurchaseListSerializer(data_objs, many=True)
                return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()
            
            else:
                data_objs = EduaddaNotesPurchase.objects.all()
                serializer = EduaddaNotesPurchaseListSerializer(data_objs, many=True)
                return CbtApiResponse(serializer.data, ApiStatus.Success).cbtResponse()
               
            
        except Exception as ex:
            return CbtApiResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse() 