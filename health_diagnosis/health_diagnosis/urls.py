"""
URL configuration for health_diagnosis project.

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
from django.urls import path
from health_diagnosis import view
from .view import ( getInfo,process_data_diabetes, process_data_parkinson, process_data_heart, process_data_hypothyroid, process_data_lungcancer, healthCheck ) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.homepage),
    path('process_diabetes/', process_data_diabetes, name='process_data_diabetes'),
    path('process_heart/', process_data_heart, name='process_data_heart'),
    path('process_hypothyroid/', process_data_hypothyroid, name='process_data_hypothyroid'),  
    path('process_parkinson/', process_data_parkinson, name='process_data_parkinson'),
    path('process_lungcancer/', process_data_lungcancer, name='process_data_lungcancer'),
    path('Health_Check/', healthCheck, name='healthCheck'),
    path('Information/', getInfo, name='getInfo'),
]
