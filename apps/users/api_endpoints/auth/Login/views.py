from rest_framework.authtoken.views import ObtainAuthToken

from apps.users.api_endpoints.auth.Login.serializers import \
    CustomAuthTokenSerializer


class CustomAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer


__all__ = ["CustomAuthToken"]
