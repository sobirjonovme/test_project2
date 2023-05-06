from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager

from rest_framework.authtoken.models import Token
from phonenumber_field.modelfields import PhoneNumberField
from django.apps import apps


class CustomUserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not phone_number:
            raise ValueError("The given phone number must be set")
        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )

        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, email, password, **extra_fields)

    def create_superuser(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone_number, email, password, **extra_fields)


class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(unique=True)
    username = None
    is_deleted = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = "phone_number"

    updated_at = models.DateTimeField(auto_now=True)

    def get_tokens(self):
        token = Token.objects.get_or_create(user=self)

        tokens = {
            "token": token.key
        }
        return tokens

    def __str__(self):
        return str(self.phone_number)

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        token = Token.objects.get_or_create(user=self)
        token.delete()
        self.save()
        return self.is_deleted
