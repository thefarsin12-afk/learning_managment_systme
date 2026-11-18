from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.core.mail import send_mail

class User(AbstractUser):

    phone = models.CharField(max_length=15,unique=True)

    ROLE_CHOICES = [
    ("trainer", "Trainer"),
    ("student", "Student"),
    
    ]

    role = models.CharField(max_length=100,choices=ROLE_CHOICES,default='student')

class TrainerProfile(models.Model):

    date_of_birth = models.DateField(null=True,blank=True)

    bio = models.TextField(null=True,blank=True)

    GENDER_OPTION = [
        ("male","male"),
        ("female","female"),
    ]

    gender = models.CharField(max_length=10,choices=GENDER_OPTION,default='male',null=True)

    profile_picture = models.ImageField(upload_to='cover_pics',null=True,blank=True)

    trainer = models.OneToOneField(User,on_delete=models.CASCADE,related_name='trainer')

    department = models.CharField(max_length=200,null=True,blank=True)

    qualification = models.CharField(max_length=200,null=True)

    linkedin_url = models.URLField(null=True)

    github_url = models.URLField(null=True)        

class StudentProfile(models.Model):

    date_of_birth = models.DateField(null=True,blank=True)

    bio = models.TextField(null=True,blank=True)

    skill = models.CharField(max_length=200,null=True)

    passout_year = models.CharField(max_length=4,null=True)

    GENDER_OPTION = [
        ("male","male"),
        ("female","female"),
    ]

    gender = models.CharField(max_length=10,choices=GENDER_OPTION,default='male',null=True)

    profile_picture = models.ImageField(upload_to='cover_pics',null=True,blank=True)

    student = models.OneToOneField(User,on_delete=models.CASCADE,related_name='student')

    qualification = models.CharField(max_length=200,null=True)

    linkedin_url = models.URLField(null=True)

    github_url = models.URLField(null=True)



def create_profile(sender,instance,created,*args,**kwargs):

    if created:

        if instance.role == 'trainer':

            TrainerProfile.objects.create(trainer=instance)

        elif instance.role == 'student':

            StudentProfile.objects.create(student=instance)

post_save.connect(create_profile,sender=User)    

def account_send_mail(sender,instance,created,*args,**kwargs):

    if created and instance.role == "trainer":

        send_mail(
            "Account creating conferamtion",
            "Trainer...You are created account👍",
            "thefarsin12@gmail.com",
            ["trock2919@gmail.com"],
    )

    elif created and instance.role == "student":

        send_mail(
            "Account creating conferamtion",
            "Student You are created account 👌.",
            "thefarsin12@gmail.com",
            ["farsinsworldshow12@gmail.com"],
    )

post_save.connect(account_send_mail,sender=User)        
