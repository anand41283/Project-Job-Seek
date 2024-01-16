from django  import forms
from jobapp.models import Category,job,student
from  django.forms import Select


class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class CategoryAdd(forms.ModelForm):
    class Meta:
        model=Category
        fields=["name"]
class JobAdd(forms.ModelForm):
    class Meta:
        model=job
        fields='__all__'   
        # widgets={
        #     'category':Select(attrs={
        #         'class': "form-select",
                
                
        #         }), 
        # }     