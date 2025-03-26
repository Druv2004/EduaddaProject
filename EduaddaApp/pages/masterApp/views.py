from django.shortcuts import render
from EduaddaApp.models import *
from django.views.decorators.clickjacking import xframe_options_exempt

# USER FORM FUNCTION HERE 
@xframe_options_exempt
def userForm(request, data_id=None):

    
    if data_id is not None:
        data_obj = EduaddaUser.objects.get(USER_ID=data_id)
        context = {'action': 'update', 'data_id': data_obj.USER_ID}
    else:
        context = {'action': 'add', 'data_id': ''}

    return render(request, 'apiForms/master-page/user/user-form.html', context)
    
