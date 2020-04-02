from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
    username = forms.CharField(label="User",max_length=20)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="PassWord",widget=forms.PasswordInput())
    password2 = forms.CharField(label="Return PassWord", widget=forms.PasswordInput())

    def clean_password2(self): # Check password
        if 'password1' in self .cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
            raise forms.ValidationError("Your PassWord is Error")
    def clean_username(self): # Check Username
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$',username):
            raise forms.ValidationError("Your UserName is Error")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Your Username is exists")
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'],email=self.cleaned_data['email'],password=self.cleaned_data['password1'])
