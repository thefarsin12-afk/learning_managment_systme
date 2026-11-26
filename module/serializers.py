from rest_framework import serializers

from module.models import Module

from lesson.models import Lessons

class ModuleSerializer(serializers.ModelSerializer):

    lesson = serializers.SerializerMethodField(read_only=True)

    lesson_count = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = Module

        fields = "__all__"

        read_only_fields = ["id","course","trainer","created_at","updated_at","module_number"]


    # def course_validation(self,validate_data):

    #     course = validate_data.get("course")

    #     if self.course not in validate_data:

    #         raise serializers.ValidationError('Course not exist')

    #     return validate_data    

    # def get_lesson(self,obj):

    #     lesson_object = Lessons.objects.filter(module=obj)



