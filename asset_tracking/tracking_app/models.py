from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length=100)
    subscription_plan = models.CharField(max_length=100, blank=True)
    subscription_start_date = models.DateField(null=True, blank=True)
    subscription_end_date = models.DateField(null=True, blank=True)
    payment_method = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='devices')
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='logs')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)  # Add this line
    checkout_date = models.DateTimeField(timezone.now())
    return_date = models.DateTimeField(null=True, blank=True)
    checkout_condition = models.TextField()
    return_condition = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.device} - {self.employee} - {self.checkout_date}"
