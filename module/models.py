from django.db import models

from course.models import Course

from accounts.models import User

class Module(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField(null=True,blank=True)

    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    trainer = models.ForeignKey(User,on_delete=models.CASCADE)

    topics = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title