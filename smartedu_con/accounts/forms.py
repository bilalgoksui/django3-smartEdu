from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder' : 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder' : 'password'
    }))
 
    # class Meta:
    #     model = User
    #     fields = ['username','password']      
        
        
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder' : 'First Name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder' : 'Last Name'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder' : 'Username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder' : 'Email'
    }))
   
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder' : 'password'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder' : 'Re-type password'
    }))
     
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']      