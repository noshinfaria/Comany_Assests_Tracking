from django.db import models
from django.contrib.auth.models import AbstractUser


# custom auth who will be a staff of a company
class CustomUser(AbstractUser):
    company = models.ForeignKey('tracking_app.Company', on_delete=models.CASCADE)
