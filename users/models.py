from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field is required')
        if not username:
            raise ValueError('The Username field is required')
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    ROLES = [
        ('Manager', 'Project Manager'),
        ('Member', 'Team Member'),
    ]
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    user_role = models.CharField(max_length=50, choices=ROLES)
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True, null=True)
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)  # Required for authentication
    is_staff = models.BooleanField(default=False)  # Required for admin access

    objects = UserManager()  # Link to custom manager

    USERNAME_FIELD = 'username'  # Field used for authentication
    REQUIRED_FIELDS = ['email']  # Required fields for creating a superuser

    def __str__(self):
        return self.username
