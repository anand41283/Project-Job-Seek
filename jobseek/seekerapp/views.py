from django.shortcuts import render,redirect
from django.views.generic import View,CreateView
from seekerapp.forms import Registration,Login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
# Create your views here.
class UserReg(CreateView):
    template_name='jobseeker/UserReg.html'
    form_class=Registration
    model=User
    success_url=reverse_lazy('Reg')

class UserLogin(View):
    def get(self,request,*args,**kwargs):
        form=Login()
        return render(request,'jobseeker/Login.html',{"form":form})
    def post(self,request,*args,**kwargs):
        form=Login(request.POST)
        if form.is_valid():
            User_name=form.cleaned_data.get('username')
            pswd=form.cleaned_data.get('password')
            user_obj=authenticate(request,username=User_name,password=pswd)
            if user_obj:
                login(request,user_obj)
                print("valid")
            else:
                print("valid")
        return redirect('Hrindex')           
