from django.contrib import admin

# Register your models here.
from .models import EmployeeInfo, Project, Leave

admin.site.register(EmployeeInfo)
admin.site.register(Project)
admin.site.register(Leave)