from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
   username = forms.CharField(label="유저id", min_length=4, max_length=30,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
   password1 = forms.CharField(label='비밀번호',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}), )
   password2 = forms.CharField(label='비밀번호 확인',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}), )
   email = forms.EmailField(label="이메일", required=False,
                            widget=forms.EmailInput(attrs={'class': 'form-control'}), )

   class Meta:
       model = User
       fields = ("username", "password1", "password2", "email")