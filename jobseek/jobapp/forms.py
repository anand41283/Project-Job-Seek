from django import forms
from django.contrib.auth.models import User

class Registerform(forms.ModelForm):
    class Meta:
        model=User
        feilds=['username','password','first_name','last_name','email']