from django.db import models
from django.contrib.auth.models import AbstractUser

from rest_framework_simplejwt.tokens import RefreshToken


# Create your models here.
class CustomUser(AbstractUser):
    updated_at = models.DateTimeField(auto_now=True)

    def get_tokens(self):
        refresh = RefreshToken.for_user(self)

        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return tokens
