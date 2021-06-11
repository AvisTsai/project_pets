from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Pet, Register


class PetForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Pet


class RegisterForm(UserCreationForm):
    username = forms.CharField(label="username")
    user_pwd = forms.CharField(label="user_pwd")
    check_password = forms.CharField(label="check_password")
    user_email = forms.EmailField(label="user_email")

    class Meta:
        model = Register
        fields = (
            'username',
            'user_pwd',
            'check_password',
            'user_email',
        )


