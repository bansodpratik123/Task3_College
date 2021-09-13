from django.urls import path
from .views import homepageView, addStudentView, showStudentView, addTeacherView, showTeacherView, addDeparmentView, showDepartmentView, updateTeacherView, deleteTeacherView
from .views import updateStudentView,deleteStudentView, searchView, searchResult


urlpatterns=[
    path('home/',homepageView, name='home'),
    path('addstudent/',addStudentView , name='addstudent'),
    path('showstudent/',showStudentView, name='showstudent'),
    path('updatestudent/<int:Student_id>/', updateStudentView, name='updatestudent'),
    path('deletestudent/<int:Student_id>/', deleteStudentView, name='deletestudent'),
    path('addteacher/',addTeacherView , name='addteacher'),
    path('showteacher/',showTeacherView, name='showteacher'),
    path('adddept/',addDeparmentView , name='adddept'),
    path('showdept/',showDepartmentView, name='showdept'),
    path('updateteacher/<int:Teacher_id>/',updateTeacherView , name='updateteacher'),
    path('deleteteacher/<int:Teacher_id>/',deleteTeacherView, name='deleteteacher'),
    path('searchview/', searchView, name='searchview'),
    path('searchresult/', searchResult, name='searchresult'),
]