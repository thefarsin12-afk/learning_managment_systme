from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from module.models import Module
from module.serializers import ModuleSerializer

from course.models import Course

class ModuleCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def post(self,request,pk=None):

        course_id = pk

        course_object = Course.objects.get(course=course_id)

        form_data = request.data

        serializer = ModuleSerializer(data=form_data)

        if serializer.is_valid():

            serializer.save(course=course_object,trainer=request.user)

            return Response(data=serializer.data)

        return Response(data=serializer.errors)

