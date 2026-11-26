from django.db import models

from course.models import Course

from accounts.models import User

class Module(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField(null=True,blank=True)

    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    trainer = models.ForeignKey(User,on_delete=models.CASCADE)

    topics = models.TextField()

    module_number = models.PositiveIntegerField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):

        last_object = Module.objects.filter(course=self.course).last()

        if last_object:

            self.module_number = last_object.module_number + 1

        else:
            self.module_number = 1

        return super().save(*args,**kwargs)            

   