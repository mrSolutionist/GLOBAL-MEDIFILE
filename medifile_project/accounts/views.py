from django.http.response import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import HospitalSignupForm, id_generator, DoctorSignupForm, PatientsSignupForm
from django.contrib.auth import authenticate, get_user_model
from hospitals.models import HospitalData
from django.contrib.auth import login, logout
from doctors.models import DoctorsData
from patients.models import PatientsData
from  django.core.mail import send_mail
from django.contrib import  messages
from django.conf import settings

user = get_user_model()
print(user)
# Create your views here.

# doctor SIgn UP


def doctor_signup(request):
    form = DoctorSignupForm()
    if request.method == 'POST':
        form = DoctorSignupForm(request.POST)
        print("one")
        if form.is_valid():
            first_name = form.cleaned_data.get("name")
            last_name = form.cleaned_data.get("last_name")
            birth = form.cleaned_data.get('birth')
            gender = form.cleaned_data.get("gender")
            phone = form.cleaned_data.get("phone")
            email = form.cleaned_data.get("email")
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            x = form.cleaned_data.get('whichHosp')
            whichHosp = x.id

            

            if password1 == password2:
                GIN = id_generator()
                
                doc = user.objects.create_doctor(GIN=GIN, password=password1, email=email,
                                                 gender=gender, birth=birth, phone=phone, name=first_name, last_name=last_name, whichHosp=whichHosp)
                docData = DoctorsData(newDoc=doc)
                subject = 'GIN NUMBER'
                message ='your global identification number is ' + GIN
                recipient = email
                send_mail(subject,message,settings.EMAIL_HOST_USER,[recipient],fail_silently = False)
                messages.success(request,'GIN sent')

                docData.save()
                
                print(user)
                if user.is_hospital:
                    return redirect('hospitalIndex')
                else:
                    return redirect('/')

        else:
            return HttpResponse("error")

    return render(request, 'registration/doctor_sign_up.html', {'form': form})


# hospital SignUp

def hospital_signup(request):
    if request.method == 'POST':
        form = HospitalSignupForm(request.POST)
        GIN = id_generator()

        # print('number',GIN)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            print(name, email, password1)
            if password1 == password2:

                hospital = user.objects.create_hospital(GIN=GIN,
                                                        email=email, name=name, password=password1)
                hospitalData = HospitalData(hospital=hospital)
                hospitalData.save()
                subject = 'GIN NUMBER'
                message ='your global identification number is ' + GIN
                recipient = email
                send_mail(subject,message,settings.EMAIL_HOST_USER,[recipient],fail_silently = False)
                messages.success(request,'GIN sent')
                new = authenticate(GIN=GIN, password=password1)
                login(request, new)
                return redirect("hospitalIndex")
        else:
            print(form.errors)
            raise ValueError("field isue")
    else:
        if request.method == "GET":

            form = HospitalSignupForm()
            return render(request, 'registration/hospital_reg.html', {'form': form})


# patients Sign up


def patient_signup(request):
    form = PatientsSignupForm()
    if request.method == 'POST':
        form = PatientsSignupForm(request.POST)
        print("one")
        if form.is_valid():

            print("2")
            first_name = form.cleaned_data.get("name")
            print(first_name)
            last_name = form.cleaned_data.get("last_name")
            print(last_name)
            birth = form.cleaned_data.get('birth')
            print(birth)
            gender = form.cleaned_data.get("gender")
            print(gender)
            phone = form.cleaned_data.get("phone")
            print(phone)
            email = form.cleaned_data.get("email")
            print(email)
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            x = form.cleaned_data.get('whichDoc')
            whichDoc = x.id
            if password1 == password2:
                GIN = id_generator()
                pat = user.objects.create_patient(GIN=GIN, password=password1, email=email,
                                                  gender=gender, birth=birth, phone=phone, name=first_name, last_name=last_name, whichDoc=whichDoc)
                patData = PatientsData(newPat=pat)
                patData.save()
                subject = 'GIN NUMBER'
                message ='your global identification number is ' + GIN
                recipient = email
                send_mail(subject,message,settings.EMAIL_HOST_USER,[recipient],fail_silently = False)
                messages.success(request,'GIN sent')
                return redirect("doctorsIndex")

        else:
            return HttpResponse("noo baby")

    return render(request, 'registration/patients_reg.html', {'form': form})


def Newlogin(request):
    if request.method == 'POST':
        GIN = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, GIN=GIN, password=password)

        if user is not None:
            login(request, user)

            if user.is_hospital:
                return redirect("hospitalIndex")

            if user.is_doctor:
                return redirect('doctorsIndex')

        else:
            form = AuthenticationForm()
            return render(request, 'registration/login.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, "registration/login.html", {'form': form})


def custom_logout(request):
    # print('Loggin out {}'.format(request.user)) check format
    user.is_active = False

    logout(request)
   
    if user.is_hospital:

        return redirect('hospitalIndex')
    else:
        return redirect('/')


def news(request):
    return render(request, 'page/news.html')
