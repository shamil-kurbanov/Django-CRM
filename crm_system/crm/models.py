# crm/models.py

from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class AdvertisingCampaign(models.Model):
    name = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    promotion_channel = models.CharField(max_length=100)
    advertising_budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class PotentialClient(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    advertising_campaign = models.ForeignKey(AdvertisingCampaign, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Contract(models.Model):
    name = models.CharField(max_length=100)
    conclusion_date = models.DateField()
    validity_period = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  # Assuming Contract is related to a Service
    document = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.name


class ActiveClient(models.Model):
    potential_client = models.OneToOneField(PotentialClient, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)

    def __str__(self):
        return self.potential_client.full_name
