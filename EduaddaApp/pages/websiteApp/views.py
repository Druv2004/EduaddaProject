from django.shortcuts import render
from EduaddaApp.models import *
from django.views.decorators.clickjacking import xframe_options_exempt

# BANNER DATA FORM
@xframe_options_exempt
def cbtBannerDataForm(request, banner_id=None):

    
        if banner_id is not None:
            data_obj = EduaddaBanner.objects.get(PR_BANNER_ID=banner_id)
            context = {'action': 'update','banner_id': data_obj.PR_BANNER_ID}
        else:
            context = {'action': 'add','banner_id': ''}
        
        return render(request, 'apiForms/website-page/banner/banner-page.html', context)


