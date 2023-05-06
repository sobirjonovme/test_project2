from django.urls import path

from apps.users.api_endpoints import auth

app_name = "users"

urlpatterns = [
    path("register/", auth.RegisterAPIView.as_view(), name="register"),
    path("user-delete/", auth.UserDeleteAPIView.as_view(), name="user-delete"),
]
