from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication

from accounts.serializers import UserSerializer
from accounts.models import User
from accounts.permission import IsOwner
from accounts.models import TrainerProfile
from accounts.serializers import TrainerProfileSerializer

class CreateTrainerView(APIView):

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

class TrainerProfileUpdateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    def put(self,request):

        form_data = request.data

        trainer_object = TrainerProfile.objects.get(trainer=request.user)

        serializer = TrainerProfileSerializer(data=form_data,instance=trainer_object)

        if serializer.is_valid():

            serializer.save()

            return Response(data=serializer.data)

        else:return Response(data=serializer.errors)

class GetMeTrainerProfileView(APIView):

    authentication_classes = [authentication.TokenAuthentication] 

    permission_classes = [IsOwner]

    def get(self,request):

        trainer = request.user

        instance = get_object_or_404(TrainerProfile,trainer=trainer)

        serializer = TrainerProfileSerializer(instance)

        return Response(data=serializer.data)

    



