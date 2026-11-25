from rest_framework import serializers

from course.models import Course

from module.models import Module
from module.serializers import ModuleSerializer

class CourseSerializer(serializers.ModelSerializer):

    module = serializers.SerializerMethodField(read_only=True)

    total_module = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = Course

        fields = "__all__"

        read_only_fields = ["id","trainer","created_at","updated_at"] 

    def get_module(self,obj):

        module_object = Module.objects.filter(course=obj)

        serializer_instants = ModuleSerializer(module_object,many=True)

        return serializer_instants.data

    def get_total_module(self,obj):

        return Module.objects.filter(course=obj).count()





