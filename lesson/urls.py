from django.urls import path

from lesson.views import LessonsCreateView
from lesson.views import LessonsRetrieveUpdateDeleteView

urlpatterns = [

    path('<int:pk>/chapter/',LessonsCreateView.as_view()),

    path('chapter/<int:pk>/',LessonsRetrieveUpdateDeleteView.as_view()),

]