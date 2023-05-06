from django.contrib.auth import authenticate
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

from apps.users.models import CustomUser


class CustomAuthTokenSerializer(serializers.Serializer):
    phone_number = PhoneNumberField(label="Phone Number", write_only=True)

    # username = serializers.CharField(
    #     label="Username",
    #     write_only=True
    # )
    password = serializers.CharField(
        label="Password",
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )
    token = serializers.CharField(
        label="Token",
        read_only=True,
    )

    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        password = attrs.get("password")

        is_exist = CustomUser.objects.filter(phone_number=phone_number, is_deleted=False).exists()
        if not is_exist:
            msg = "Unable to log in with provided credentials."
            raise serializers.ValidationError(msg, code="authorization")

        if phone_number and password:
            user = authenticate(request=self.context.get("request"), username=phone_number, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = "Unable to log in with provided credentials."
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = 'Must include "phone_number" and "password".'
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs
