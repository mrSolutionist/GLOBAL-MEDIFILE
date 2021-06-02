from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
user = get_user_model()


def doctorsIndex(request):
    pats = user.objects.filter(is_patient=True, whichDoc=request.user.id)
    

    totalPats = pats.count()
    context = {'pats': pats, 'totalPats': totalPats}
    return render(request, 'page/doctors_index.html', context)
