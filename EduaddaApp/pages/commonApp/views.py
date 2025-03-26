from django.shortcuts import render
from EduaddaApp.models import *
from django.views.decorators.clickjacking import xframe_options_exempt

# COURSE DATA FORM
@xframe_options_exempt
def cbtCourseDataForm(request, course_id=None):

    
        if course_id is not None:
            data_obj = EduaddaCourse.objects.get(COURSE_ID=course_id)
            context = {'action': 'update','course_id': data_obj.COURSE_ID}
        else:
            context = {'action': 'add','course_id': ''}
        
        return render(request, 'apiForms/common-page/course/course-page.html', context)
    
# NOTES DATA FORM
@xframe_options_exempt
def cbtNotesDataForm(request, notes_id=None):

    
        if notes_id is not None:
            data_obj = EduaddaNotes.objects.get(NOTES_ID=notes_id)
            context = {'action': 'update','notes_id': data_obj.NOTES_ID}
        else:
            context = {'action': 'add','notes_id': ''}
        
        return render(request, 'apiForms/common-page/notes/notes-page.html', context)


