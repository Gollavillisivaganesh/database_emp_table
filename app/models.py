from django.db import models

# Create your models here.
class Dept(models.Model):
    Deptno=models.IntegerField(primary_key=True)
    Dname=models.CharField(max_length=100)
    Loc=models.CharField(max_length=100)
    def __str__(self):
        return self.Dname

class Emp(models.Model):
    Empno=models.IntegerField()
    Ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    mgr=models.IntegerField()
    Hiredate=models.DateField()
    Sal=models.IntegerField()
    Comm=models.IntegerField(null=True)
    Deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    def __str__(self):
        return self.job
