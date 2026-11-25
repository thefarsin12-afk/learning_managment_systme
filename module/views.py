from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication

from module.permission import IsCourseTrainer
from module.serializers import ModuleSerializer

from course.models import Course

class ModuleCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsCourseTrainer]

    def post(self,request,pk=None):

        course_id = pk

        course_object = get_object_or_404(Course,id=course_id)

        self.check_object_permissions(request,course_object)

        form_data = request.data

        serializer = ModuleSerializer(data=form_data)

        if serializer.is_valid():

            serializer.save(course=course_object,trainer=request.user)

            return Response(data=serializer.data)

        return Response(data=serializer.errors)

