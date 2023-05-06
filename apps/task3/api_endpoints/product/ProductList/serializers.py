from rest_framework import serializers

from apps.task3.models import Product
from apps.task3.services.encoders import aes_encrypt


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(method_name="encrypt_name")
    description = serializers.SerializerMethodField(method_name="encrypt_description")
    price = serializers.SerializerMethodField(method_name="encrypt_price")
    marja = serializers.SerializerMethodField(method_name="encrypt_marja")
    package_code = serializers.SerializerMethodField(method_name="encrypt_package_code")

    class Meta:
        model = Product
        fields = ("name", "description", "price", "marja", "package_code")

    def encrypt_name(self, obj):
        return aes_encrypt(obj.name)["cipher_text"]

    def encrypt_description(self, obj):
        return aes_encrypt(obj.description)["cipher_text"]

    def encrypt_price(self, obj):
        return aes_encrypt(str(obj.price))["cipher_text"]

    def encrypt_marja(self, obj):
        return aes_encrypt(str(obj.marja))["cipher_text"]

    def encrypt_package_code(self, obj):
        return aes_encrypt(obj.package_code)["cipher_text"]
