from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from users.models import RegDoctor, RegPatient
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.template import RequestContext
from .forms import LoginForm


def index(request):
    if request.method == 'GET':
        return render(request, 'users/index.html', {'form': AuthenticationForm()})
    elif request.method == 'POST':
        email = request.POST['patient_login']
        password = request.POST['patient_pass']
        patient_user = RegPatient.objects.get(email=email)
        if patient_user.check_password(password):
            return redirect('patientProfile')
        else:
            return redirect('index')
        # user_doc = RegDoctor.objects.filter(email)
        # user_doc = authenticate(request, user_doc)
        # if user_doc is None:
            #         return render(request, 'users/index.html', {'form': AuthenticationForm(), 'error': "Can't find that email address"})
            #     else:
            #         login(request, user_doc)
            #         return redirect('docProfile')

            # form = RegDoctor(request.POST)
            # email = request.POST['doc_login']
            # password = request.POST['doc_pass']
            # doc_login = auth.authenticate(email=email, password=password)
            # auth.login(request, doc_login)
            # if doc_login is not None:
            #     return redirect('docProfile')
            # else:
            #     return redirect('index')


def regDoctor(request):
    if request.method == 'GET':
        return render(request, 'users/regDoctor.html', {'form': UserCreationForm()})
    if request.method == 'POST':
        username = request.POST['doctor_id']
        first_name = request.POST['doc_fname']
        last_name = request.POST['doc_lname']
        email = request.POST['doc_Email']
        password = request.POST['doc_pass1']
        confirm_password = request.POST['doc_pass2']
        date_of_birth = request.POST['doc_dob']
        gender = request.POST['doc_gender']
        license_no = request.POST['doc_license']
        university = request.POST['university']
        referral_id = request.POST['ref_id']
        city = request.POST['doc_city']
        country = request.POST['doc_country']
        zip_code = request.POST['doc_zip']
        phone = request.POST['doc_phone']

        # Check Username

        if RegDoctor.objects.filter(username=username).exists():
            return render(request, 'users/regDoctor.html', {'form': UserCreationForm(), 'error': "That username has already been taken. Please chose a new username"})
        if RegDoctor.objects.filter(email=email).exists():
            return render(request, 'users/regDoctor.html', {'form': UserCreationForm(), 'error': "That email has already been taken. Please chose a new email"})
        if password == confirm_password:
            user_doc = RegDoctor.objects.create_user(
                username=username, first_name=first_name, last_name=last_name, email=email, password=password, date_of_birth=date_of_birth, gender=gender, license_no=license_no, university=university, referral_id=referral_id, city=city, country=country, zip_code=zip_code, phone=phone)
            user_doc.save()
            user_doc = authenticate(RegDoctor, email=email, password=password)
            login(request, user_doc)
            return redirect('index')
        else:
            return render(request, 'users/regDoctor.html', {'form': UserCreationForm(), 'error': "Passwords did not match"})


def doc_login(request):
    if request.method == 'GET':
        return render(request, 'users/docLogin.html', {'form': UserCreationForm()})
    elif request.method == 'POST':
        # form = LoginForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     cd = form.cleaned_data
        # doc_user = authenticate(
        #     request, email=cd['doc_email'], password=cd['doc_pass'])
        email = request.POST['doc_email']
        password = request.POST['doc_pass']
        # doc_user = authenticate(RegDoctor.objects.get(email=email), password=password)
        doc_user = RegDoctor.objects.get(email=email)
        if doc_user.check_password(password):
            if doc_user is not None:
                if doc_user.is_active:
                    doc_user = authenticate(
                        request, email=email, password=password)
                    context = {'username': doc_user.username}
                    login(request, doc_user)
                    return render(request, 'users/docProfile.html', context_instance=RequestContext(request))
                    # {'username': doc_user.username}
                else:
                    return HttpResponse('Disabled account')
    else:
        return redirect('index')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


def regPatient(request):
    if request.method == 'GET':
        return render(request, 'users/regPatient.html', {'form': UserCreationForm()})
    if request.method == 'POST':
        username = request.POST['patient_id']
        first_name = request.POST['patient_fname']
        last_name = request.POST['patient_lname']
        email = request.POST['patient_email']
        password = request.POST['patientPass1']
        confirm_password = request.POST['patientPass2']
        date_of_birth = request.POST['patient_dob']
        gender = request.POST['patient_gender']
        city = request.POST['patient_city']
        country = request.POST['patient_country']
        zip_code = request.POST['patient_zip']
        phone = request.POST['patient_phone']

        # Check Username

        if RegPatient.objects.filter(username=username).exists():
            return render(request, 'users/regDoctor.html', {'form': UserCreationForm(), 'error': "That username has already been taken. Please chose a new username"})
        if RegPatient.objects.filter(email=email).exists():
            return render(request, 'users/regDoctor.html', {'form': UserCreationForm(), 'error': "That email has already been taken. Please chose a new email"})
        if password == confirm_password:
            user_patient = RegPatient.objects.create_user(
                username=username, first_name=first_name, last_name=last_name, email=email, password=password, date_of_birth=date_of_birth, gender=gender, city=city, country=country, zip_code=zip_code, phone=phone)
            user_patient.save()
            login(request, user_patient)
            return redirect('patientProfile')
        else:
            return render(request, 'users/patientProfile.html', {'form': UserCreationForm(), 'error': "Passwords did not match"})


def docProfile(request):
    return render(request, 'users/docProfile.html')


def patientProfile(request):
    return render(request, 'users/patientProfile.html')
