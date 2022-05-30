from django.db import models
import datetime
# Create your models here.



class Employee(models.Model):
    name = models.CharField(max_length=50,null=True)
    team_leader=models.CharField(max_length=50,null=True)
    designation = models.CharField(max_length=50,null=True)
    experience = models.CharField(max_length=20,null=True)
    stack = models.CharField(max_length=50,null=True)        
    # secondary_skills = models.CharField(max_length=50,null=True)
    skills = models.CharField(max_length=50,null=True)
    resource_status = models.CharField(max_length=50,null=True)
    date_of_joining= models.CharField(max_length=50,null=True)
    # date_of_joining= models.DateField(blank=True,default=datetime.date.today)
    
    # work_status = models.CharField(max_length=50,null=True) 
    # billing = models.BooleanField(default=False,null=True)
    # pay_value = models.FloatField(null=True)
    # proxy = models.BooleanField(default=False,null=True)
    profile_link = models.CharField(max_length=50,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
