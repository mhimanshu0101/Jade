from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.core.management.utils import get_random_secret_key

from engine.utils import timezone

# Create your models here.
class UserType:
    EMPLOYEE = 1
    STAFF = 2
    PARTNER = 3
    CUSTOMER = 4
    AGGREGATOR = 5

class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICE = (
        (None, 'Please select user type'),
        (UserType.EMPLOYEE, 'Employee'),
        (UserType.STAFF, 'Staff'),
        (UserType.PARTNER, 'Partner'),
        (UserType.CUSTOMER, 'Customer'),
        (UserType.AGGREGATOR, 'Aggregator')
    )
    # user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICE, blank=True, null=True)
    email = models.EmailField(max_length=256, blank=True, null=True, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now_local)
    token_secret_key = models.CharField(max_length=128, default=get_random_secret_key, unique=True)
    referral_code = models.CharField(max_length=32, blank=True, null=True)
    USERNAME_FIELD = 'email'

    # class Meta:
    #     verbose_name_plural = 'Users'

    def __str__(self) -> str:
        return self.email or self.id or ''