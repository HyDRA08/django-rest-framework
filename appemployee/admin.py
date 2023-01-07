from django.contrib import admin
from appemployee.models import EmployeeModel,DepartmentModel
# Register your models here.
admin.site.register(EmployeeModel)
admin.site.register(DepartmentModel)