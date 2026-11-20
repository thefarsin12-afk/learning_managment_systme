from django.urls import path

from course.views import CourseListCreateView
from course.views import CourseRetrieveUpdateDeleteView

urlpatterns = [

    # course list,create
    path('courses/',CourseListCreateView.as_view()),

    # course retrieve,update,delete
    path('courses/<int:pk>/',CourseRetrieveUpdateDeleteView.as_view()),


]