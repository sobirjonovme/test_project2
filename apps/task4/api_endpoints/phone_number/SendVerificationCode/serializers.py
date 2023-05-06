from rest_framework import serializers

from apps.task4.models import PhoneNumber


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = (
            "full_name",
            "phone_number",
        )
