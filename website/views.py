from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from EduaddaApp.models import *
import json

def base(request):
    user_id = request.session.get('user_id')  # Assuming you store user_id in session
    user = None
    if user_id:
        user = EduaddaUser.objects.get(USER_ID=user_id)
    context = {
        'user': user  # Pass the logged-in user to the template
    }
    return render(request, 'eduaddaWebsitePages/base.html', context)
def home(request):
    banner = EduaddaBanner.objects.filter(PR_STATUS=1)
    course = EduaddaCourse.objects.filter(STATUS=1)
    notes = EduaddaNotes.objects.filter(STATUS=1)
    context = {
        'banners': banner,  
        'courses':course,
        'notes':notes,
        'navbar' : 'home'
    }
    return render(request,'eduaddaWebsitePages/home.html',context)

def course(request):
    class_12th_courses = EduaddaCourse.objects.filter(CATEGORY=1)  # CATEGORY 1: Class 12th
    cuet_courses = EduaddaCourse.objects.filter(CATEGORY=2)  # CATEGORY 2: CUET

    context = {
        'class_12th_courses': class_12th_courses,
        'cuet_courses': cuet_courses,
        'navbar' : 'course'
    }
    return render(request,'eduaddaWebsitePages/course.html', context)

def notes(request):
    class_12th_notes = EduaddaNotes.objects.filter(CATEGORY=1)  # CATEGORY 1: Class 12th
    cuet_notes = EduaddaNotes.objects.filter(CATEGORY=2)  # CATEGORY 2: CUET

    context = {
        'class_12th_notes': class_12th_notes,
        'cuet_notes': cuet_notes,
        'navbar' : 'notes'
    }
    return render(request,'eduaddaWebsitePages/notes.html',context)

def review(request):
    review = EduaddaReview.objects.filter(STATUS=1)
    context = {
         'navbar' : 'review',
         'review': review
    }
    return render(request,'eduaddaWebsitePages/review.html',context)

def myPurchase(request):
    user_id = request.session.get('user_id')  # Ensure this matches your session key

    if not user_id:
        # Redirect to login if user_id is not found
        return redirect('/login')  # Replace with the actual login URL

    try:
        # Fetch the user object
        user = EduaddaUser.objects.get(USER_ID=user_id)
    except EduaddaUser.DoesNotExist:
        # If the user_id in session is invalid, redirect to login
        return redirect('/login')

    # Fetch purchased courses and related course details
    purchased_courses = EduaddaCoursePurchase.objects.filter(USER=user).select_related('COURSE')
    purchased_notes = EduaddaNotesPurchase.objects.filter(USER=user).select_related('NOTE')

    # Extract the courses for easier access in the template
    purchased_courses = [purchase.COURSE for purchase in purchased_courses]
    purchased_notes = [notes.NOTE for notes in purchased_notes]

    # Fetch purchased notes (if applicable)

    # Pass the data to the template
    context = {
        'purchased_courses': purchased_courses,
        'purchased_notes': purchased_notes,
    }
    return render(request, 'eduaddaWebsitePages/myPurchase.html', context)

 
    
    
    
def login(request):
    context = {

    }
    return render(request,'eduaddaWebsitePages/login.html',context)

def signUp(request):
    context = {

    }
    return render(request,'eduaddaWebsitePages/signUp.html',context)

def profile(request):
    context = {
        'navbar' : 'profile'
    }
    return render(request,'eduaddaWebsitePages/profile.html',context)

def forgetPassword(request):
    context = {
        
    }
    return render(request,'eduaddaWebsitePages/forgetPassword.html',context)