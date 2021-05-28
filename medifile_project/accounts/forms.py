from django.contrib.auth.forms import UserCreationForm
from django import forms as f
from django.contrib.auth import get_user_model
import random
import string
user = get_user_model()


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].help_text = None


class HospitalSignupForm(CustomUserCreationForm):

    class Meta:
        model = user
        fields = ('name', 'email')


class DoctorSignupForm(CustomUserCreationForm):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = f.CharField(widget=f.TextInput(
        attrs={'class': 'input--style-4', 'placeholder': 'first name'}))
    last_name = f.CharField(widget=f.TextInput(
        attrs={'class': 'input--style-4', 'placeholder': 'last name'}))
    email = f.EmailField(widget=f.EmailInput(
        attrs={'class': 'input--style-4', 'placeholder': 'email'}))
    gender = f.ChoiceField(choices=GENDER_CHOICES, widget=f.RadioSelect(
        attrs={'class':'d-inline-flex'}))

    birth = f.DateField(widget=f.DateInput(
        attrs={'class': 'input--style-4', 'placeholder': 'birthday'}))

    phone = f.IntegerField(widget=f.TextInput(
        attrs={'class': 'input--style-4', 'placeholder': 'phone number'}))

    password1 = f.CharField(widget=f.PasswordInput(
        attrs={'class': 'input--style-4', 'placeholder': 'password'}))
    password2 = f.CharField(widget=f.PasswordInput(
        attrs={'class': 'input--style-4', 'placeholder': 'retype'}))

    class Meta:
        model = user
        fields = ('email', 'name', 'last_name',
                  'phone', 'birth','gender')



class PatientsSignupForm(CustomUserCreationForm):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = f.CharField(widget=f.TextInput(
        attrs={'class': 'input--style-4', 'placeholder': 'first name'}))
    last_name = f.CharField(widget=f.TextInput(
        attrs={'class': 'input--style-4', 'placeholder': 'last name'}))
    email = f.EmailField(widget=f.EmailInput(
        attrs={'class': 'input--style-4', 'placeholder': 'email'}))
    gender = f.ChoiceField(choices=GENDER_CHOICES, widget=f.RadioSelect(
        attrs={'class':'d-inline-flex'}))

    birth = f.DateField(widget=f.DateInput(
        attrs={'class': 'input--style-4', 'placeholder': 'birthday'}))

    phone = f.IntegerField(widget=f.TextInput(
        attrs={'class': 'input--style-4', 'placeholder': 'phone number'}))

    password1 = f.CharField(widget=f.PasswordInput(
        attrs={'class': 'input--style-4', 'placeholder': 'password'}))
    password2 = f.CharField(widget=f.PasswordInput(
        attrs={'class': 'input--style-4', 'placeholder': 'retype'}))

    class Meta:
        model = user
        fields = ('email', 'name', 'last_name',
                  'phone', 'birth','gender')
