from django.shortcuts import render, redirect
from .forms import PatientDetailForm

# Create your views here.


def conditionDetail(request):
    form = PatientDetailForm()

    if request.method == "POST":
        form = PatientDetailForm(request.POST)
        if form.is_valid():
            medical_condition = form.cleaned_data.get('medical_condition')

            condition_description = form.cleaned_data.get('condition_description')

            prescription = form.cleaned_data.get('prescription')

            summary = form.cleaned_data.get('summary')

            









            return redirect('doctorsIndex')

    return render(request, 'registration/patientDetail.html', {'form': form})
