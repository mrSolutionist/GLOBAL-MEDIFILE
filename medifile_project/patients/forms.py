from django.contrib.auth.forms import  forms



class PatientDetailForm(forms.Form):

    name = forms.CharField(max_length=200)

    last_name = forms.CharField(max_length=200)

    GIN = forms.CharField(max_length=200)

    # medical_condition  = forms.CharField(max_length=400)

    # condition_description = forms.CharField(max_length=400)

    # # media_files = forms.ImageField()

    # prescription = forms.CharField(max_length=400)

    # summary = forms.CharField(max_length=400)

    

