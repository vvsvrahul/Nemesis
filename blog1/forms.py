from django import forms
from django.forms import ModelForm
from blog1.models import *
from django.contrib.auth.models import User

# class BlogForm(forms.ModelForm):
#     class Meta():
#         model = 'BlogContent'
#         fields = ('Title','content')


class authenticateform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields =('username','email')

# class BlogContent1Form(forms.ModelForm):
#     class Meta():
#         model = BlogContent11
#         fields = ('title','story')

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']