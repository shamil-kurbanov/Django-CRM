# crm/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Service
from .forms import ServiceForm, AdvertisingCampaignForm, PotentialClientForm, ContractForm

from rest_framework import viewsets
from .models import Service, AdvertisingCampaign, PotentialClient, Contract, ActiveClient
from .serializers import ServiceSerializer, AdvertisingCampaignSerializer, PotentialClientSerializer, \
    ContractSerializer, ActiveClientSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class AdvertisingCampaignViewSet(viewsets.ModelViewSet):
    queryset = AdvertisingCampaign.objects.all()
    serializer_class = AdvertisingCampaignSerializer


class PotentialClientViewSet(viewsets.ModelViewSet):
    queryset = PotentialClient.objects.all()
    serializer_class = PotentialClientSerializer


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class ActiveClientViewSet(viewsets.ModelViewSet):
    queryset = ActiveClient.objects.all()
    serializer_class = ActiveClientSerializer


@login_required
def services_view(request):
    services = Service.objects.all()
    return render(request, 'crm/services_list.html', {'services': services})


@login_required
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'crm/service_create.html', {'form': form})


@login_required
def service_update(request, pk):
    service = Service.objects.get(pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'crm/service_update.html', {'form': form})


@login_required
def service_delete(request, pk):
    service = Service.objects.get(pk=pk)
    service.delete()
    return redirect('service_list')


@login_required
def advertising_campaign_list(request):
    campaigns = AdvertisingCampaign.objects.all()
    return render(request, 'crm/advertising_campaign_list.html', {'campaigns': campaigns})


@login_required
def advertising_campaign_create(request):
    if request.method == 'POST':
        form = AdvertisingCampaignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('advertising_campaign_list')
    else:
        form = AdvertisingCampaignForm()
    return render(request, 'crm/advertising_campaign_create.html', {'form': form})


@login_required
def advertising_campaign_update(request, pk):
    campaign = AdvertisingCampaign.objects.get(pk=pk)
    if request.method == 'POST':
        form = AdvertisingCampaignForm(request.POST, instance=campaign)
        if form.is_valid():
            form.save()
            return redirect('advertising_campaign_list')
    else:
        form = AdvertisingCampaignForm(instance=campaign)
    return render(request, 'crm/advertising_campaign_update.html', {'form': form})


@login_required
def advertising_campaign_delete(request, pk):
    campaign = AdvertisingCampaign.objects.get(pk=pk)
    campaign.delete()
    return redirect('advertising_campaign_list')


# ------------ PotentialClientForm -------------------------

@login_required
def potential_client_list(request):
    potential_clients = PotentialClient.objects.all()
    return render(request, 'crm/potential_client_list.html', {'potential_clients': potential_clients})


@login_required
def potential_client_create(request):
    if request.method == 'POST':
        form = PotentialClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('potential_client_list')
    else:
        form = PotentialClientForm()
    return render(request, 'crm/potential_client_create.html', {'form': form})


@login_required
def potential_client_update(request, pk):
    client = PotentialClient.objects.get(pk=pk)
    if request.method == 'POST':
        form = PotentialClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('potential_client_list')
    else:
        form = PotentialClientForm(instance=client)
    return render(request, 'crm/potential_client_update.html', {'form': form})


@login_required
def potential_client_delete(request, pk):
    client = PotentialClient.objects.get(pk=pk)
    client.delete()
    return redirect('potential_client_list')


# ------------ End PotentialClientForm -------------------------


# ------------ Contracts -----------------------------------------
def contract_list(request):
    contracts = Contract.objects.all()
    return render(request, 'crm/contract_list.html', {'contracts': contracts})


def contract_create(request):
    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            contract = form.save(commit=False)
            # Assuming you're getting service_id from the form or somewhere else
            contract.save()
            return redirect('contract_list')
    else:
        form = ContractForm()
    return render(request, 'crm/contract_create.html', {'form': form})


def contract_update(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('contract_list')
    else:
        form = ContractForm(instance=contract)
    return render(request, 'crm/contract_update.html', {'form': form})


def contract_delete(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    if request.method == 'POST':
        contract.delete()
        return redirect('contract_list')
    return render(request, 'crm/contract_delete.html', {'contract': contract})


def contract_detail(request, pk):
    contract = get_object_or_404(Contract, pk=pk)
    return render(request, 'crm/contract_detail.html', {'contract': contract})

# ------------ End Contracts -------------------------
