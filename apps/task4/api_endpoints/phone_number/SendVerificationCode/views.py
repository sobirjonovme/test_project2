from django.core.cache import cache
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.task4.api_endpoints.phone_number.SendVerificationCode.serializers import \
    PhoneNumberSerializer
from apps.task4.services.generators import (generate_session,
                                            generate_verification_code)
from apps.task4.services.sms_sender import send_verification_code_sms


class PhoneRegisterAPIView(APIView):
    @swagger_auto_schema(request_body=PhoneNumberSerializer)
    def post(self, request, *args, **kwargs):
        serializer = PhoneNumberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        session = generate_session()

        phone_number = data["phone_number"]
        # if cache.get(phone_number, None) is not None:
        #     # If phone number already exists in cache
        #     return Response(
        #         data={"error": "Verification code is already sent. Please wait for a while before continue"},
        #         status=status.HTTP_400_BAD_REQUEST
        #     )

        # if phone number is available
        code = generate_verification_code()
        send_verification_code_sms(phone_number, code)
        session_data = {
            "full_name": data["full_name"],
            "phone_number": phone_number,
            "code": code,
        }
        cache.set(session, session_data, 120)

        data.update({"session": session})
        return Response(data=data, status=status.HTTP_200_OK)


__all__ = ["PhoneRegisterAPIView"]
