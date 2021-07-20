from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Pet, Register, Money


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


# 記帳
class MoneyForm(forms.ModelForm):
    # category = forms.ChoiceField()
    item = forms.TextInput()
    price = forms.NumberInput()

    class Meta:
        model = Money
        fields = '__all__'

        # widgets = {
        #     'time': forms.TimeField(attrs={'class': 'form-control'}),
        #     'kind-choices': forms.ChoiceField(attrs={'class': 'form-control'}),
        #     'item': forms.TextInput(attrs={'class': 'form-control'}),
        #     'price': forms.NumberInput(attrs={'class': 'form-control'})
        # }
        # label = {
        #     'time': '時間',
        #     'kind-choices': '類別',
        #     'item': '項目',
        #     'price': '價格',
        # }
