
from secrets import choice
from django.db import models
from django.conf import settings

# Create your models here.
class User(models.Model):
    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
    )
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    username = models.CharField(max_length=10,default='username')
    Password  = models.CharField(max_length=6, default='1234')
    gender = models.CharField(max_length=10, choices=GENDER,default='Others')
    email = models.EmailField()
   
    def __str__(self):
        return f'{self.firstname}-{self.lastname}'

   
class Task(models.Model):
    STATUS = (
        ('Completed', 'Completed'),
        ('In Progress', 'In Progress'),
        ('Yet to start', 'Yet to start')
    )

    date_created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
    target_date = models.DateField()
    target_time = models.TimeField()
    content = models.TextField(max_length=200)
    status = models.CharField(max_length=200,null=True,choices=STATUS)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

