from django.db import models
from django.contrib.auth.hashers import check_password as check_password_hash

class CustomUser(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # You can use Django's built-in password hashing mechanism
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.email
    
    

