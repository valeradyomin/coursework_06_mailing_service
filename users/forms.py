from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User
from django import forms


class StyleFormMiXin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_active':
                field.widget.attrs['class'] = 'form-control'


class LoginViewForm(StyleFormMiXin, AuthenticationForm):

    class Meta:
        model = User
        fields = '__all__'


class UserRegisterForm(StyleFormMiXin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)