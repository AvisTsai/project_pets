from django import forms
from django.contrib.auth.models import User
from .models import Pet, Register, Money, MemberManagement
from django.forms import ModelForm, DateInput
from pets.models import Event


class PetForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Pet


class RegisterForm(ModelForm):
    username = forms.CharField(
        label='帳號：',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    user_pwd = forms.CharField(
        label='密碼：',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    check_password = forms.CharField(
        label='確認密碼：',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    user_email = forms.EmailField(
        label='電子郵件：',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Register
        # fields = "__all__"
        fields = ( 'username', 'user_pwd', 'check_password', 'user_email')


class LoginForm(ModelForm):
    username = forms.CharField(
        label='帳號：',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    user_pwd = forms.CharField(
        label='密碼：',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


# 記帳
class MoneyForm(forms.ModelForm):
    class Meta:
        model = Money
        fields = "__all__"

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


# calendar
class EventForm(ModelForm):
    class Meta:
        model = Event
        # datetime-local is a HTML5 input type, format to make date time show on fields
        # format datetime在html上
        widgets = {
            'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
        }
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        # datetime input設定
        # 用於嘗試將字符串轉換為有效datetime.datetime對象的格式列表
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
