from rest_framework import serializers
from .models import Employee


class EmployeeSerializers(serializers.ModelSerializer):
    name = serializers.CharField(required=False, max_length=225)
    email = serializers.EmailField(required=False, max_length=225, allow_null=False)
    job = serializers.CharField(required=False, max_length=225, allow_null=False)

    class Meta:
        model = Employee
        fields = ('name', 'email', 'job',)