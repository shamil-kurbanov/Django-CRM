# crm/serializers.py

from rest_framework import serializers
from .models import Service, AdvertisingCampaign, PotentialClient, Contract, ActiveClient


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class AdvertisingCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisingCampaign
        fields = '__all__'


class PotentialClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PotentialClient
        fields = '__all__'


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'


class ActiveClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveClient
        fields = '__all__'
