from django.db import models

from accounts.models import User

class Course(models.Model):

    title = models.CharField(max_length=200)

    language = models.CharField(max_length=200)

    description = models.TextField(null=True,blank=True)

    trainer = models.ForeignKey(User,on_delete=models.CASCADE)

    duration = models.CharField(max_length=200)

    price = models.CharField(max_length=100,null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

       return self.title