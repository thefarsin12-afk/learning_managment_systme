from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.serializers import UserSerializer
from accounts.models import User

class CreateAdminView(APIView):

    def post(self,request):

        form_data = request.data

        serializer = UserSerializer(data=form_data)

        if serializer.is_valid():

            cleaned_data = serializer.validated_data

            instance = User.objects.create_superuser(role="trainer",**cleaned_data)

            serializer = UserSerializer(instance)

            return Response(data=serializer.data)

        return Response(data=serializer.errors)

class CreateSudentView(APIView):

    def post(self,request):

        form_data = request.data

        serialzier = UserSerializer(data=form_data)

        if serialzier.is_valid():

            cleaned_data = serialzier.validated_data

            qs = User.objects.create_user(**cleaned_data,role="student")

            serialzier = UserSerializer(qs)

            return Response(data=serialzier.data)

        return Response(data=serialzier.errors)    