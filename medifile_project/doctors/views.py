from django.contrib.auth import get_user_model
from django.shortcuts import render
from hospitals.models import HospitalData
# Create your views here.
user = get_user_model()


def doctorsIndex(request):
   
    hospital =  user.objects.get(id=request.user.whichHosp) 
    print (hospital)
    pats = user.objects.filter(is_patient=True, whichDoc=request.user.id)
    print (pats)

    totalPats = pats.count()
    context = {'pats': pats, 'totalPats': totalPats,'hospital':hospital}
    return render(request, 'page/doctors_index.html', context)
