from django.db import models

# Create your models here.

class Departments(models.Model):
    DeptName=models.CharField(max_length=50)

    def __str__(self):
        return self.DeptName

class Students(models.Model):
    RollNo=models.IntegerField()
    Name=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    DeptStudent=models.ForeignKey(Departments, on_delete=models.CASCADE, )

    def __str__(self):
        return f'{self.RollNo}, {self.Name}, {self.Address}, {self.DeptStudent}'

class Teachers(models.Model):
    Name=models.CharField(max_length=50)
    Subject=models.CharField(max_length=50)
    DeptTeacher = models.ManyToManyField(Departments)
    # Department = models.ForeignKey(Departments, on_delete=models.CASCADE,default="")

    def __str__(self):
        return f'{self.Name}, {self.Subject}, {self.DeptTeacher}'

