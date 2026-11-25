from django.urls import path

from module.views import  ModuleCreateView

urlpatterns = [

    path('<int:pk>/unit/',ModuleCreateView.as_view()),

    
]