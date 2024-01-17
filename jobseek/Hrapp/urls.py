from django.urls import path
from Hrapp.views import HrLogin,Hrindex,Addcategory,Deletecategory,Addjob,Joblist,Jobdelete,JobUpdate


urlpatterns = [
    path('login/',HrLogin.as_view(),name="Hrlogin"),
    path('index/',Hrindex.as_view(),name="Hrindex"),
    path('Add category/',Addcategory.as_view(),name="Add_category"),
    path('Delete category/<int:pk>',Deletecategory.as_view(),name="Delete_category"),
    path('AddJob/',Addjob.as_view(),name="Add_job"),
    path('Joblist/',Joblist.as_view(),name="joblist"),
    path('Jobdelete/<int:pk>',Jobdelete.as_view(),name="jobdelete"),
    path('Jobupdate/<int:pk>',JobUpdate.as_view(),name="jobupdate"),
    
    
    
]
