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
        
        
class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder' : 'First Name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder' : 'Last Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder' : 'Email'
    }))

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder' : 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder' : 'password'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder' : 'Re-type password'
    }))
     
    class Meta:
        model = User
        fields = ['first_name','last_name','email','phone','username','password','password2']      