from django.urls import path

from apps.task4.api_endpoints import phone_number

app_name = "task4"

urlpatterns = [
    path("register-phone/", phone_number.PhoneRegisterAPIView.as_view(), name="register-phone-number"),
    path("verify-code/", phone_number.VerifyCodeAPIView.as_view(), name="verify-code"),
]
