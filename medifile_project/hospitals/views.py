from django.contrib.auth import get_user_model
from django.shortcuts import render


# Create your views here.

user = get_user_model()

def hospitalIndex(request):
    docs = user.objects.filter(is_doctor=True,whichHosp=request.user.id)
    print(request.user.id)
    
    totalDocs = docs.count()
    context = {'docs':docs,'totalDocs':totalDocs}
    
    return render(request, 'page/hospital_index.html',context)