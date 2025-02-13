from django.urls import path
from . import views

urlpatterns = [
    # USER FORM URL HERE
    path('user-form/', views.userForm),
    path('user-form/<int:data_id>', views.userForm),

]