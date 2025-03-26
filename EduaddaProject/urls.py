"""
URL configuration for EduaddaProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('master-api/', include('EduaddaApp.apis.masterApis.urls')),
    path('master-page/', include('EduaddaApp.pages.masterApp.urls')),
    
    path('common-api/', include('EduaddaApp.apis.commonApis.urls')),
    path('common-page/', include('EduaddaApp.pages.commonApp.urls')),
    
    path('website-api/', include('EduaddaApp.apis.websiteApis.urls')),
    path('website-page/', include('EduaddaApp.pages.websiteApp.urls')),
    
    path('', include('website.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
