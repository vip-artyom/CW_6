from enum import Enum
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from skymarket.settings import MEDIA_ROOT
from users.managers import UserManager


class UserRoles(Enum):
    ADMIN = 'admin'
    USER = 'user'


class CustomUser(AbstractBaseUser):
    ROLE_CHOICES = [(UserRoles.ADMIN.value, 'admin'),
                    (UserRoles.USER.value, 'user'), ]

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default=UserRoles.USER.value)
    image = models.ImageField(upload_to=MEDIA_ROOT, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'custom_user'

    @property
    def is_superuser(self):
        return self.role == UserRoles.ADMIN.value

    @property
    def is_staff(self):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    objects = UserManager()
