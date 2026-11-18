from rest_framework import serializers

from accounts.models import User
from accounts.models import TrainerProfile
from accounts.models import StudentProfile

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ['id','username','email','password','phone','role']

        extra_kwargs = {
            'password': {'write_only': True},
            'role': {'read_only': True}
        }

class TrainerProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = TrainerProfile

        fields = "__all__"

        read_only_fields = ['id','trainer']

class StudentProfileSerailizer(serializers.ModelSerializer):

    class Meta:

        model = StudentProfile 

        fields = "__all__"

        read_only_fields = ["id","student"]       