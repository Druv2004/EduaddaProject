from django.urls import path
from . import views


urlpatterns = [
    path('base',views.base,name='base'),
    path('',views.home,name='home'),
    path('course',views.course,name='course'),
    path('notes',views.notes,name='notes'),
    path('review',views.review,name='review'),
    path('my-purchase',views.myPurchase,name='myPurchase'),
    path('login',views.login,name='login'),
    path('sign-up',views.signUp,name='signUp'),
    path('profile',views.profile,name='profile'),
    path('forget-password',views.forgetPassword,name='forgetPassword'),
    
    
]