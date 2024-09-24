from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_status = models.CharField(max_length=30, default='Basic')
    registration_date = models.DateField(auto_now_add=True)
