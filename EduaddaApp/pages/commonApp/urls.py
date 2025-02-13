from django.urls import path
from . import views

urlpatterns = [

    # COURSE DATA FORM URL HERE
    path('course-form', views.cbtCourseDataForm),
    path('course-form/<int:course_id>', views.cbtCourseDataForm),
    
    # COURSE DATA FORM URL HERE
    path('notes-form', views.cbtNotesDataForm),
    path('notes-form/<int:notes_id>', views.cbtNotesDataForm),
    
    
]
