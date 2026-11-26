from django.urls import path

from module.views import  ModuleCreateView
from module.views import ModuleRetriveUpdateDeleteView

urlpatterns = [

    path('<int:pk>/unit/',ModuleCreateView.as_view()),

    path('unit/<int:pk>/',ModuleRetriveUpdateDeleteView.as_view()),

    
]