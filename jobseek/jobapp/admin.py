from django.contrib import admin
from jobapp.models import job,student,Category

# Register your models here.

admin.site.register(job)
admin.site.register(Category)
admin.site.register(student)