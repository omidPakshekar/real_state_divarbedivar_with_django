from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(LoginForm, self).__init__(*args, **kwargs)

    password = forms.CharField(label=': کلمه عبور',
         widget=forms.PasswordInput(
                     attrs={
                         "style" :"text-align:right; ",
                         "class" : " wrap-input100 main validate-input input100 ",
                         "id" : "f22",
                         "placeholder" :"کلمه عبور"
                         }
        )
     )
    username = forms.CharField(label=':نام کاربری',
        widget=forms.TextInput(
            attrs={
                 "style" :"text-align:right; ",

                "class" : " wrap-input100 main validate-input input100 ",
                "id" : "f22",
                "placeholder" : "نام کاربری"
                }
            )
        )
    remember_me = forms.BooleanField(required=False,label='مرا به خاطر بسپار',
            widget=forms.CheckboxInput(
                attrs={
                    "style" : "margin-top:5px; float:right; margin-right:5px;",
                    }
                )
                )
