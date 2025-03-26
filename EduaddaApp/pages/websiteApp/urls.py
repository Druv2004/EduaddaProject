from django.urls import path
from . import views

urlpatterns = [

    # BANNER DATA FORM URL HERE
    path('banner-form', views.BannerDataForm),
    path('banner-form/<int:banner_id>', views.BannerDataForm),
    
    # REVIEW DATA FORM URL HERE
    path('review-form', views.ReviewDataForm),
    path('review-form/<int:review_id>', views.ReviewDataForm),
    
    
]
