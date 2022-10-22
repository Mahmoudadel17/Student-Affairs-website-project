from re import T
from django.db import models


ge = [
    ('Female','Female'),
    ('Male','Male')
]
lev = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4')

]
dep = [
    ('General','General'),
    ('CS','CS'),
    ('IT','IT'),
    ('IS','IS'),
    ('AI','AI'),
    ('DS','DS')
]

st = [
    ('Active','Active'),
    ('InActive','InActive')
]

class Student(models.Model):
    Name = models.CharField(max_length=60,null=True)
    id = models.CharField(max_length=8,primary_key=True)
    Email = models.EmailField(max_length= 25)
    Gender = models.CharField(max_length=6,choices=ge) 
    MobileNumber = models.CharField(max_length=11)
    Date_of_birth = models.DateField(null=True)
    GPA = models.DecimalField(max_digits=3,decimal_places=2,null=True)
    status = models.CharField(max_length=8,choices=st)
    level = models.CharField(max_length=1,choices=lev)
    Department = models.CharField(max_length=7,choices=dep)


    def __str__(self):
        return self.Name
    
    class Meta: 
        ordering = ['Name']
    
    
     
