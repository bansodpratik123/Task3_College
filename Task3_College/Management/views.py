from django.shortcuts import render,redirect
from .forms import StudentModelForm, TeacherModelForm, DepartmentModelForm
from .models import Students, Teachers, Departments


# Create your views here.
def homepageView(request):
    template_name='Management/Homepage.html'
    context={}
    return render(request,template_name,context)

def addStudentView(request):
    form=StudentModelForm()
    if request.method=='POST':
        form=StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showstudent')
    template_name='Management/AddStudent.html'
    context={'form':form}
    return render(request,template_name,context)

def showStudentView(request):
    records=Students.objects.all()
    template_name='Management/ShowStudent.html'
    context={'records':records}
    return render(request,template_name,context)

def updateStudentView(request,Student_id):
    record=Students.objects.get(id=Student_id)
    form=StudentModelForm(instance=record)
    if request.method=='POST':
        form=StudentModelForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            return redirect('showstudent')
    template_name='Management/UpdateStudent.html'
    context={'form':form}
    return render(request,template_name,context)

def deleteStudentView(request,Student_id):
    record=Students.objects.get(id=Student_id)
    record.delete()
    return redirect('showstudent')


def addTeacherView(request):
    form=TeacherModelForm()
    if request.method=='POST':
        form=TeacherModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showteacher')
    template_name='Management/AddTeacher.html'
    context={'form':form}
    return render(request,template_name,context)

def updateTeacherView(request,Teacher_id):
    record=Teachers.objects.get(id=Teacher_id)
    form=TeacherModelForm(instance=record)
    if request.method=='POST':
        form=TeacherModelForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            return redirect('showteacher')
    template_name='Management/UpdateTeacher.html'
    context={'form':form}
    return render(request,template_name,context)

def deleteTeacherView(request,Teacher_id):
    record=Teachers.objects.get(id=Teacher_id)
    record.delete()
    return redirect('showteacher')


def showTeacherView(request):
    records=Teachers.objects.all()
    template_name='Management/ShowTeacher.html'
    context={'records':records}
    return render(request,template_name,context)

def addDeparmentView(request):
    form=DepartmentModelForm()
    if request.method=='POST':
        form=DepartmentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showdept')
    template_name='Management/AddDepartment.html'
    context={'form':form}
    return render(request,template_name,context)

def showDepartmentView(request):
    records=Departments.objects.all()
    template_name='Management/ShowDepartment.html'
    context={'records':records}
    return render(request,template_name,context)

def searchView(request):
    template_name = 'Management/SearchPage.html'
    if request.method=='POST':
        n=request.POST.get('search')
        print(n)
        records_Student = Students.objects.filter(Name=n)
        print(n)
        records_Teacher=Teachers.objects.filter(Name=n)
        print(n)
        context = {'records_Teacher': records_Teacher,'records_Student':records_Student}
        print(n)
        return render(request,template_name,context)
        print('After return')

    context={}
    return render(request,template_name,context)

def searchResult(request):
    n=request.POST.get('search')
    print(n)
    records_Teacher=Teachers.objects.filter(Name=n)

    context={'records_Teacher':records_Teacher}
    template_name = 'Management/SearchResult.html'
    return render(request,template_name,context)

