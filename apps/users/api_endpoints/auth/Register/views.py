from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.api_endpoints.auth.Register.serializers import \
    RegisterSerializer
from apps.users.models import CustomUser


class RegisterAPIView(APIView):
    def post(self, request):
        data = request.data
        users = CustomUser.objects.filter(phone_number=data["phone_number"], is_deleted=True)

        if users.exists():
            user = users.first()
            data.update({"is_deleted": False})
            serializer = RegisterSerializer(user, data=data)
        else:
            serializer = RegisterSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save(is_deleted=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


__all__ = ["RegisterAPIView"]
