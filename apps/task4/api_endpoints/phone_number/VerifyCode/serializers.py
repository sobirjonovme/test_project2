from rest_framework import serializers


class VerifyCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    session = serializers.CharField(max_length=32)
    code = serializers.CharField(max_length=6)
