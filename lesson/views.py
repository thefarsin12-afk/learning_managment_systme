from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.generics import RetrieveUpdateDestroyAPIView


from lesson.serializer import LessonsSerializer

from lesson.models import Lessons

from module.models import Module


class LessonsCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def post(self,request,pk=None):

        module_id = pk

        module_object = get_object_or_404(Module,id=module_id)

        form_data = request.data

        serializer_instance = LessonsSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save(module=module_object,created_by=request.user)

            return Response(data=serializer_instance.data)

        return Response(data=serializer_instance.errors)


class LessonsRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    serializer_class = LessonsSerializer

    queryset = Lessons.objects.all()

