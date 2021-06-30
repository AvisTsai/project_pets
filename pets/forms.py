from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Pet, Register


class PetForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Pet


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label="帳號")
    user_pwd = forms.CharField(label="密碼")
    check_password = forms.CharField(label="確認密碼")
    user_email = forms.EmailField(label="電子郵件")

    class Meta:
        model = Register
        fields = (
            'username',
            'user_pwd',
            'check_password',
            'user_email',
        )


