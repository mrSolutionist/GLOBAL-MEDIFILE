from django.contrib.auth import forms
from django.contrib.auth import get_user_model
import random,string
user=get_user_model()



def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

class HospitalSignupForm(forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(HospitalSignupForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None
    class Meta:
        model = user
        fields = ('name', 'email')


class DoctorSignupForm(forms.UserCreationForm):
    class Meta:
        model = user
        fields = ('email',)

