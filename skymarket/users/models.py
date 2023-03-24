from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from skymarket.settings import MEDIA_ROOT
from users.managers import UserManager, UserRoles


class User(AbstractBaseUser):

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone = PhoneNumberField()
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=5, choices=UserRoles.choices, default=UserRoles.USER)
    image = models.ImageField(upload_to=MEDIA_ROOT, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role']

    class Meta:
        db_table = 'user'

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
