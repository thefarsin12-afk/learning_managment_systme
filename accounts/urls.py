from django.urls import path
from accounts.views import CreateAdminView
from accounts.views import CreateSudentView

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [

    # trainer registraion
    path('trainer/register/',CreateAdminView.as_view()),

    # trainer token genareting
    path('trainer/loggin/',ObtainAuthToken.as_view()),

    # student registraion
    path('student/register/',CreateSudentView.as_view()),
    
    # student jwt loggin
    path('student/jwt/loggin/',TokenObtainPairView.as_view()),
    path('student/jwt/refresh/loggin/',TokenRefreshView.as_view()),

]