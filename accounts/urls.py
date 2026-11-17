from django.urls import path
from accounts.views import CreateAdminView
from accounts.views import CreateSudentView

urlpatterns = [

    # trainer registraion
    path('trainer/register/',CreateAdminView.as_view()),
    path('student/register/',CreateSudentView.as_view()),

]