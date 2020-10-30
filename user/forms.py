from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserData


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
    


class UserDataForm(forms.ModelForm):
    GENDER_CHOICES = [('male', 'MALE'), ('female', 'FEMALE'), ('others', 'OTHERS')]
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)
    class Meta:
        model = UserData
        fields = '__all__'
        exclude = ['user']