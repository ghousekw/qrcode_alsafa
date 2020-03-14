from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    profession = models.CharField(max_length=250, null=True)
    email = models.EmailField(unique=True, max_length=250)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    website = models.CharField(max_length=250, null=True)
    social_link = models.CharField(max_length=250, null=True, blank=True)
    activity = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Users'
        db_table = 'User'


class Company(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='company_user')
    company_name = models.CharField(max_length=300, null=True, blank=True)