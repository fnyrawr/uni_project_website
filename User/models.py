from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


# Create your models here.
class CustomUser(AbstractUser):
    ROLES = [
        ('S', 'Superuser'),
        ('M', 'CapybaraStudios Member'),
        ('U', 'User'),
    ]
    email = models.EmailField(blank=True, unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    role = models.CharField(max_length=2,
                            choices=ROLES,
                            default='U',
                            )
    is_verified = models.BooleanField(default=False)

    def is_authorized(self):
        return self.is_superuser_or_group_member()

    def is_superuser_or_group_member(self):
        if self.role == 'S' or self.role == 'M':
            return True
        else:
            return False

    def __str__(self):
        return self.username