from django.http.response import HttpResponse
from django.contrib.auth.forms import  AuthenticationForm
from django.shortcuts import render, redirect
from .forms import HospitalSignupForm, id_generator ,DoctorSignupForm
from django.contrib.auth import authenticate, get_user_model
from hospitals.models import HospitalData
from django.contrib.auth import login

user = get_user_model()
print(user)
# Create your views here.


def doctor_signup(request):
    form = DoctorSignupForm(request.POST)
    if request.method == 'POST':
        form = DoctorSignupForm(request.POST)
        if form.is_valid():
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            
    return render(request, 'registration/doctor_sign_up.html',{'form':form})


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

            form = HospSignupForm()
            return render(request, 'registration/hospital_reg.html', {'form': form})


def Newlogin(request):
    if request.method == 'POST':
        GIN = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, GIN=GIN, password=password)

        if user is not None:
            login(request,user)

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
