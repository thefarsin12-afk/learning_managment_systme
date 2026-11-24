from django.urls import path

from module.views import  ModuleCreateView

urlpatterns = [

    path('unit/',ModuleCreateView.as_view()),

    
]