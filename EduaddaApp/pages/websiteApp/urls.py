from django.urls import path
from . import views

urlpatterns = [

    # BANNER DATA FORM URL HERE
    path('banner-form', views.cbtBannerDataForm),
    path('banner-form/<int:banner_id>', views.cbtBannerDataForm),
    
    
]
