from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class SigninForm(UserCreationForm):
    password1 = password2 = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control my-2 border border-3'}))
    first_name = last_name = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control my-2 border border-3'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control my-2 border border-3'}),
            'email' : forms.EmailInput(attrs={'class':'form-control my-2 border border-3'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2 border border-3'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control my-2 border border-3'}))

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        authenticated_user = authenticate(username = username, password = password)

        if not authenticated_user or not authenticated_user.is_active:
            raise forms.ValidationError("Username and password are invalid!")
            
        return cleaned_data
