from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser
)
import uuid
from user.managers import UserManager

import random


def generate_connection_id():
    return random.randint(1000000000, 9999999999)


# ! custom user model
class User(AbstractBaseUser):
    id = models.URLField(
        primary_key=True, default=uuid.uuid4, auto_created=True)

    username = models.CharField(
        max_length=50,
        unique=False,
        blank=False,
    )

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        error_messages={
            "unique": "This email is already taken."
        }
    )

    profile = models.ImageField(upload_to="uploads", blank=True)

    connection_id = models.BigIntegerField(
        default=generate_connection_id, auto_created=True, unique=True)

    date_of_birth = models.DateField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
