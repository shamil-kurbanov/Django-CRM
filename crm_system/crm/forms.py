# crm/forms.py

from django import forms
from .models import Service
from .models import AdvertisingCampaign
from .models import PotentialClient
from .models import Contract


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class AdvertisingCampaignForm(forms.ModelForm):
    class Meta:
        model = AdvertisingCampaign
        fields = ['name', 'service', 'promotion_channel', 'advertising_budget']


class PotentialClientForm(forms.ModelForm):
    class Meta:
        model = PotentialClient
        fields = ['full_name', 'phone', 'email', 'advertising_campaign']


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['name', 'conclusion_date', 'validity_period', 'amount', 'document', 'service']
        widgets = {
            'conclusion_date': forms.DateInput(attrs={'type': 'date'}),
            'validity_period': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add a field for selecting the service
        self.fields['service'].queryset = Service.objects.all()  # Assuming Service is the related model