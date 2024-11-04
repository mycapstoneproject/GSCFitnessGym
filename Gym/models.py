
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from django import forms





class Member(models.Model):
    members_ID = models.AutoField(primary_key=True)  # Unique ID
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True)  # Optional
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=50, null=True,)
    email_address = models.CharField(max_length=50,null=True )
    GENDERS_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
       
    ]
    gender = models.CharField(max_length=1, choices=GENDERS_CHOICES, default='M')
    phone_number = models.CharField(max_length=20,null=True,)
    pricing = models.DecimalField(max_digits=10, decimal_places=2,null=True,)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    active = models.BooleanField(default=True)
    def __str__(self):
      return f"{self.first_name} {self.last_name}"

    

class Trainer(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    middle_name = models.CharField(max_length=30, null=True)  
    last_name = models.CharField(max_length=30, null=True)
    age = models.PositiveIntegerField(null=True)
    address = models.CharField(max_length=50, null=True,)
    phone_number = models.CharField(max_length=100, null=True)
    email_address = models.CharField(max_length=50,null=True )


    salary = models.IntegerField(default=0)
    active = models.BooleanField(default=True)


    def __str__(self):
      return f"{self.first_name} {self.last_name}"
    

class Notification(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email_address = models.CharField(max_length=50,null=True )
    message = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name


class Attendance(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField(default=timezone.now) 
    present = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.member} - {self.date} {'Present' if self.present else 'Absent'}"
    


