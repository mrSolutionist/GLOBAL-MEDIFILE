from django.http.response import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import HospitalSignupForm, id_generator, DoctorSignupForm, PatientsSignupForm
from django.contrib.auth import authenticate, get_user_model
from hospitals.models import HospitalData
from django.contrib.auth import login
from doctors.models import DoctorsData
from patients.models import PatientsData

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
            whichHosp = form.cleaned_data.get('whichHosp')
            if password1 == password2:
                GIN = id_generator()
                doc = user.objects.create_doctor(GIN=GIN, password=password1, email=email,
                                                 gender=gender, birth=birth, phone=phone, name=first_name, last_name=last_name)
                docData = DoctorsData(newDoc=doc)
                docData.save()
                return HttpResponse("doc added")

        else:
            return HttpResponse("noo baby")

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
                new = authenticate(GIN=GIN, password=password1)
                login(request, new)
                return redirect("index")
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
            if password1 == password2:
                GIN = id_generator()
                pat = user.objects.create_patient(GIN=GIN, password=password1, email=email,
                                                  gender=gender, birth=birth, phone=phone, name=first_name, last_name=last_name)
                patData = PatientsData(newPat=pat)
                patData.save()
                return HttpResponse("pat added")

        else:
            return HttpResponse("noo baby")

    return render(request, 'registration/patient_sign_up.html', {'form': form})


def Newlogin(request):
    if request.method == 'POST':
        GIN = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, GIN=GIN, password=password)

        if user is not None:
            login(request, user)

            if user.is_hospital:
                return HttpResponse("hosp")

            if user.is_doctor is True:
                return HttpResponse("doc")

        else:
            form = AuthenticationForm()
            return render(request, 'registration/login.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, "registration/login.html", {'form': form})
