from django import forms
from .models import Departments, Students, Teachers

class StudentModelForm(forms.ModelForm):
    class Meta:
        model=Students
        fields='__all__'

class TeacherModelForm(forms.ModelForm):
    class Meta:
        model=Teachers
        fields='__all__'

class DepartmentModelForm(forms.ModelForm):
    class Meta:
        model=Departments
        fields='__all__'