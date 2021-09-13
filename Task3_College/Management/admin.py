from django.contrib import admin
from .models import Students, Teachers, Departments

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['RollNo','Name','Address','DeptStudent']
admin.site.register(Students,StudentAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['Name','Subject']
admin.site.register(Teachers,TeacherAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['DeptName']
admin.site.register(Departments,DepartmentAdmin)