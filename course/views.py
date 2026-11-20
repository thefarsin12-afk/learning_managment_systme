from django.shortcuts import render

from rest_framework import authentication,permissions
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from course.serializer import CourseSerializer
from course.models import Course
from course.permission import IsTrainer

class CourseListCreateView(ListCreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    serializer_class = CourseSerializer

    queryset = Course.objects.all()

    def perform_create(self, serializer):
        serializer.save(trainer=self.request.user)

class CourseRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsTrainer]

    serializer_class = CourseSerializer

    queryset = Course.objects.all()    