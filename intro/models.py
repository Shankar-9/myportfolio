from django.db import models

# Create your models here.
class Journey(models.Model):
    university=models.CharField(max_length = 1000)
    description=models.TextField()
    from_date=models.DateField()
    to_date=models.DateField()
    extra=models.TextField()
class Journey1(models.Model):
    university=models.CharField(max_length = 1000)
    description=models.TextField()
    from_date=models.DateField()
    to_date=models.DateField()
    extra=models.TextField()
class projects(models.Model):
    title=models.CharField(max_length=1000)
    description=models.TextField()
    skills=models.TextField()
    gitlink=models.URLField()
    livelink=models.URLField()
    certificatelink=models.URLField()
class skills(models.Model):
    STATUS_CHOICES=(('P', 'programme'),('T', 'technology'))
    skill=models.CharField(max_length=200)
    type=models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')
    image=models.ImageField(upload_to='pics/')
    