from django.urls import path
from . import views

urlpatterns = [
    # BANNER API's URL HERE
    path('banner-add', views.EduaddaBannerViewSet.as_view({'post': 'bannerAdd'})),
    path('banner-update', views.EduaddaBannerViewSet.as_view({'post': 'bannerUpdate'})),
    path('banner-list', views.EduaddaBannerViewSet.as_view({'post': 'bannerList'})),
]
