from django.shortcuts import render
from EduaddaApp.models import *
from django.views.decorators.clickjacking import xframe_options_exempt

# BANNER DATA FORM
@xframe_options_exempt
def BannerDataForm(request, banner_id=None):

    
        if banner_id is not None:
            data_obj = EduaddaBanner.objects.get(PR_BANNER_ID=banner_id)
            context = {'action': 'update','banner_id': data_obj.PR_BANNER_ID}
        else:
            context = {'action': 'add','banner_id': ''}
        
        return render(request, 'apiForms/website-page/banner/banner-page.html', context)
    
# REVIEW DATA FORM
@xframe_options_exempt
def ReviewDataForm(request, review_id=None):

    
        if review_id is not None:
            data_obj = EduaddaReview.objects.get(REVIEW_ID=review_id)
            context = {'action': 'update','review_id': data_obj.REVIEW_ID}
        else:
            context = {'action': 'add','review_id': ''}
        
        return render(request, 'apiForms/website-page/review/review-page.html', context)


