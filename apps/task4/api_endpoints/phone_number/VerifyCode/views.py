from django.core.cache import cache
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.task4.api_endpoints.phone_number.VerifyCode.serializers import \
    VerifyCodeSerializer
from apps.task4.models import PhoneNumber


class VerifyCodeAPIView(APIView):
    @swagger_auto_schema(request_body=VerifyCodeSerializer)
    def post(self, request, *args, **kwargs):
        serializer = VerifyCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # get values from request data
        phone_number = serializer.validated_data["phone_number"]
        session = serializer.validated_data["session"]
        code = serializer.validated_data["code"]

        cache_data = cache.get(session, None)
        print(cache_data)

        if cache_data is None:
            # if nothing is found with given phone number
            return Response(
                data={"error": "Verification code is expired!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if cache_data["code"] != code:
            # if incorrect code is entered
            return Response(data={"error": "Incorrect Code!"})

        if cache_data["phone_number"] != phone_number:
            # if incorrect code is entered
            return Response(data={"error": "Incorrect phone number!"})

        # if everything is OKAY
        cache_data.pop("code")
        record = PhoneNumber(**cache_data)
        record.save()

        # return response
        return Response(data={"message": "Phone number registered successfully!"}, status=status.HTTP_200_OK)


__all__ = ["VerifyCodeAPIView"]
