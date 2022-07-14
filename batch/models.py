from django.db import models
from s3direct.fields import S3DirectField
from rest_framework import serializers

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])

# Create your models here.
class Material(models.Model):
    material = models.FileField(upload_to='studymaterial/', null=True, verbose_name="")
    
    def _str_(self):
       return self.material

class StudyMaterial(models.Model):
   
    title=models.CharField(max_length=50)
    material = models.FileField(upload_to='studymaterial/', null=True, verbose_name="")
    batch_code=models.IntegerField(default=220101)
    # material = models.ManyToManyField(Material)
    def __str__(self):
        return self.title

class Courses(models.Model):
  
    title=models.CharField(max_length=50)
    video= models.FileField(upload_to='videos/', null=True, verbose_name="")
    batch_code=models.IntegerField(default=220101)
    # thumbnail = models.ImageField(upload_to='thumbnail/', blank=True, null=True)
    def __str__(self):
        return self.title

class Batches(models.Model):
    batch_code=models.IntegerField(primary_key=True)
    batch_start=models.DateTimeField()
    course=models.CharField(max_length=50)
    category=models.CharField(max_length=10, null=True, blank=True)
    subject=models.CharField(max_length=20, null=True, blank=True)
    

    def __str__(self):
        return str(self.batch_code)



class Profile(models.Model):
    name=models.CharField(max_length=60)
    dob=models.DateField()
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=100)
    image = models.ImageField(upload_to=nameFile, blank=True, null=True)
    subscription_start_date=models.DateField()
    subscription_end_date=models.DateField()
    password=models.CharField(max_length=50)
    batch_codes=models.ManyToManyField(Batches)
    # course_codes = CourseCode()
    # course_codes=models.CharField(max_length=10, default="[]")
    def __str__(self):
        return self.name

class Notification(models.Model):
    TYPES = [
            ('Announcement','Announcement'),
            ('Live Classes','Live Classes'),
            ('New Video','New Video'),

    ]
    title=models.CharField(max_length=50)
    notif_type=models.CharField(max_length=50,choices=TYPES , default='New Video')
    desc=models.CharField(max_length=500)
    def __str__(self):
        return self.title

class Admin(models.Model):
    username=models.CharField(max_length=50, unique=True)
    password=models.CharField(max_length=50)
    def __str__(self):
        return str(self.username)

