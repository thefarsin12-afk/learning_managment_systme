from django.db import models

from accounts.models import User

from module.models import Module

class Lessons(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField(null=True,blank=True)

    module = models.ForeignKey(Module,on_delete=models.CASCADE)

    video_url = models.URLField(null=True,blank=True)

    duration = models.CharField(max_length=50,null=True,blank=True)

    lesson_number = models.PositiveIntegerField()

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.title

    def save(self,*args,**kwargs):

        last_object = Lessons.objects.filter(module=self.module).last()

        if last_object:

            self.lesson_number = last_object.lesson_number + 1

        else:
            self.lesson_number = 1

        return super().save(*args,**kwargs)

