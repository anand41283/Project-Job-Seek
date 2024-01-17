from django.urls import path
from seekerapp.views import UserReg,UserLogin

urlpatterns=[
    path('Userreg/',UserReg.as_view(),name="Reg"),
    path('Userlogin/',UserLogin.as_view(),name="Login")
]