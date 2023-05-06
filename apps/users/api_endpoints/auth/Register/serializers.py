from rest_framework import serializers

from apps.users.models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "phone_number", "password")

    def to_representation(self, instance):
        data = super(RegisterSerializer, self).to_representation(instance)
        data.update(instance.get_tokens())
        return data
