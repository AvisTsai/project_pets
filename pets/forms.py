from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Pet, Register, Money
from django.forms import ModelForm, DateInput
from pets.models import Event


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
        self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
        self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)