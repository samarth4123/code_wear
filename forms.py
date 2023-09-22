from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,SetPasswordForm,PasswordResetForm
from django import forms
from django.contrib.auth.models import User
from .models import Customer


class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class CustomerRegistrationForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True','class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class PasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label='Old Password' ,widget=forms.PasswordInput(attrs={'autofocus':'True','autocomplete':'current-password','class':'form-control'}))
    new_password1=forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2=forms.CharField(label='Confirm Password' ,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class PasswordResetForm(PasswordResetForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))

class PasswordSetForm(SetPasswordForm):
    new_password1=forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    new_password2=forms.CharField(label='Confirm Password' ,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['Name','Locality','City','Mobile','Zipcode','State']
        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Locality':forms.TextInput(attrs={'class':'form-control'}),
            'City':forms.TextInput(attrs={'class':'form-control'}),
            'Mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'Zipcode':forms.NumberInput(attrs={'class':'form-control'}),
            'State':forms.Select(attrs={'class':'form-control'}),

        }
