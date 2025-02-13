from django.urls import path
from . import views

urlpatterns = [
        
    # USER API's URL HERE
    path('user-list', views.CbtUserViewSet.as_view({'post': 'userList'})),
    # path('user-data-list', views.CbtUserViewSet.as_view({'post': 'userDataList'})),
    path('user-register', views.CbtUserViewSet.as_view({'post': 'userRegister'})),
    path('user-login', views.CbtUserViewSet.as_view({'post': 'userLogin'})),
    path('user-logout', views.CbtUserViewSet.as_view({'post': 'userLogout'})),
    path('user-profile', views.CbtUserViewSet.as_view({'post': 'userProfile'})),
    path('user-profile-update', views.CbtUserViewSet.as_view({'post': 'userProfileUpdate'})),
    path('forget-password', views.CbtUserViewSet.as_view({'post': 'forgetPassword'})),
    path('change-password', views.CbtUserViewSet.as_view({'post': 'changePassword'})),

]