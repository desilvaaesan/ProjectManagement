from django.db import models

class User(models.Model):
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
    contact_info = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.username
