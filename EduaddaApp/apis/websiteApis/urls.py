from django.urls import path
from . import views

urlpatterns = [
    # BANNER API's URL HERE
    path('banner-add', views.EduaddaBannerViewSet.as_view({'post': 'bannerAdd'})),
    path('banner-update', views.EduaddaBannerViewSet.as_view({'post': 'bannerUpdate'})),
    path('banner-list', views.EduaddaBannerViewSet.as_view({'post': 'bannerList'})),
    
    # REVIEW API's URL HERE
    path('review-add', views.EduaddaReviewViewSet.as_view({'post': 'reviewAdd'})),
    path('review-update', views.EduaddaReviewViewSet.as_view({'post': 'reviewUpdate'})),
    path('review-list', views.EduaddaReviewViewSet.as_view({'post': 'reviewList'})),
]
