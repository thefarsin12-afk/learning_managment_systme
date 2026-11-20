from rest_framework import serializers

from course.models import Course

class CourseSerializer(serializers.ModelSerializer):

    class Meta:

        model = Course

        fields = "__all__"

        read_only_fields = ["id","trainer","created_at","updated_at"] 