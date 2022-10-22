from django.contrib import admin
from .models import Student


 

admin.site.register(Student)

admin.site.site_header = 'Student Affairs website'
admin.site.site_title = 'Student Affairs website'
