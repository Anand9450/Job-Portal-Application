from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StudentUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=15, null=True)
    experience = models.CharField(max_length=100, null=True)
    skills = models.CharField(max_length=100, null=True)
    social_link = models.URLField(null=True)
    resume = models.FileField(null=True)

    def __str__(self):
        return self.user.username

class Recruiter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15, null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10, null=True)
    company = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=15, null=True)
    status = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user.username


class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=100)
    salary = models.FloatField(max_length=50, null=True)
    image = models.FileField()
    description = models.CharField(max_length=2000, null=True)
    experience = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    creation_date = models.DateField()

    def __str__(self):
        return self.title

class Apply(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE)
    resume = models.FileField(null=True)
    apply_date = models.DateField()
    status = models.CharField(max_length=20, default="Pending")
    cover_letter = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.id)