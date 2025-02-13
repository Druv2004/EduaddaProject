from django.urls import path
from . import views

urlpatterns = [
    path('file-data-upload', views.EduaddaFileDataViewSet.as_view({'post': 'fileDataUpload'})),

    #======================= COURSE URL ==========================
    path('course-add', views.EduaddaCourseDataViewSet.as_view({'post': 'courseAdd'})),
    path('course-update', views.EduaddaCourseDataViewSet.as_view({'post': 'courseUpdate'})),
    path('course-list', views.EduaddaCourseDataViewSet.as_view({'post': 'courseList'})),
    
    #======================= NOTES URL ==========================
    path('notes-add', views.EduaddaNotesDataViewSet.as_view({'post': 'notesAdd'})),
    path('notes-update', views.EduaddaNotesDataViewSet.as_view({'post': 'notesUpdate'})),
    path('notes-list', views.EduaddaNotesDataViewSet.as_view({'post': 'notesList'})),
    
    
    #======================= PURCHASE COURSE URL ==========================
    path('course-purchase', views.EduaddaCoursePurchaseDataViewSet.as_view({'post': 'purchaseCourse'})),
    path('course-purchase-list', views.EduaddaCoursePurchaseDataViewSet.as_view({'post': 'purchaseCourseList'})),
    
    
    #======================= PURCHASE NOTES URL ==========================
    path('notes-purchase', views.EduaddaNotesPurchaseDataViewSet.as_view({'post': 'purchaseNotes'})),
    path('notes-purchase-list', views.EduaddaNotesPurchaseDataViewSet.as_view({'post': 'purchaseNotesList'})),

    #======================= CREATE ORDER ==========================
    path('create-razorpay-order/', views.create_razorpay_order, name='create_razorpay_order'),    
    path('create-razorpay-order-notes/', views.create_razorpay_order_notes, name='create_razorpay_order'),    
]