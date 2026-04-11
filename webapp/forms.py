from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from . models import *
 #REGISTER USER
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        exclude = ['create_at']
        
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        exclude = ['create_at']