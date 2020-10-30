from django import  forms
from .models import Contact
# from user.models import UserData



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


# class UserDataForm(forms.ModelForm):
#     class Meta:
#         model = UserData
#         fields = '__all__'
#         exclude = ['user']