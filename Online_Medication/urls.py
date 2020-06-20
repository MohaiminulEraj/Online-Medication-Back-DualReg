"""Online_Medication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from users import views as user_views
from articles import views as article_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.index, name='index'),
    path("Register-as-a-Doctor/", user_views.regDoctor, name='regDoctor'),
    path('Login-as-a-Doctor', user_views.doc_login, name='doc_login'),
    path('Register-as-a-Patient/', user_views.regPatient, name='regPatient'),
    path('Write-an-Article/', article_view.editorpanel, name='editorpanel'),
    path('Doctors-Profile', user_views.docProfile, name='docProfile'),
    path('Patients-Profile', user_views.patientProfile, name='patientProfile'),
    path('', user_views.logoutuser, name='logoutuser'),
]
