from django.shortcuts import render,redirect
from django.views.generic import View,FormView,TemplateView,CreateView,ListView,UpdateView
from Hrapp.forms import Loginform,CategoryAdd,JobAdd
from jobapp.models import Category,job,student
from django.urls import reverse_lazy

# Create your views here.
class HrLogin(FormView):
    template_name='login.html'
    form_class=Loginform

class Hrindex(TemplateView):
    template_name='index.html'

class Addcategory(CreateView,ListView):
    template_name='Add_category.html'
    form_class=CategoryAdd
    model=Category
    success_url=reverse_lazy("Add_category")
    context_object_name="data"

class Deletecategory(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Category.objects.get(id=id).delete()
        return redirect('Add_category')
    
class Addjob(CreateView):
    template_name='Add_job.html'
    form_class=JobAdd
    model=job
    success_url=reverse_lazy('Hrindex')
class Joblist(ListView):
    template_name='Joblist.html'
    model=job
    context_object_name="jobs"   
class Jobdelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk') 
        job.objects.get(id=id).delete()
        return redirect("joblist")   
class JobUpdate(UpdateView):
    template_name='Jobupdate.html'
    form_class=JobAdd
    model=job
    success_url=reverse_lazy('joblist')





    



