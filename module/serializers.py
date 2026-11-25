from rest_framework import serializers

from module.models import Module

class ModuleSerializer(serializers.ModelSerializer):

    class Meta:

        model = Module

        fields = "__all__"

        read_only_fields = ["id","course","trainer","created_at","updated_at","module_number"]