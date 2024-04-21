from typing import Any
from uuid import uuid4

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str, **extra_fields: dict[str, Any]) -> Any:
        if not email:
            raise ValueError(_("The Email must be set"))
        if not password:
            raise ValueError(_("The Password must be set"))

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email: str, password: str, **extra_fields) -> Any:
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_active") is not True:
            raise ValueError(_("Superuser must have is_active=True."))
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    uuid = models.UUIDField(default=uuid4, editable=False)
    email = models.EmailField(_("email address"), unique=True, db_index=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]

    objects = UserManager()

    class Meta:
        db_table = "users"

    def __str__(self) -> str:
        return self.email
