# crm/urls.py

from django.urls import path, include
from rest_framework import routers
from .views import (ServiceViewSet,
                    AdvertisingCampaignViewSet,
                    PotentialClientViewSet,
                    ContractViewSet,
                    ActiveClientViewSet,
                    services_view,
                    service_create,
                    service_update,
                    service_delete,
                    advertising_campaign_list,
                    advertising_campaign_create,
                    advertising_campaign_update,
                    advertising_campaign_delete,
                    potential_client_list, potential_client_create, potential_client_update, potential_client_delete,
                    contract_list, contract_create, contract_update, contract_delete, contract_detail,
                    )
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
# router.register(r'services', ServiceViewSet)
# router.register(r'advertising_campaigns', AdvertisingCampaignViewSet)
# router.register(r'potential_clients', PotentialClientViewSet)
# router.register(r'contracts', ContractViewSet)
# router.register(r'active_clients', ActiveClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('services/', services_view, name='service_list'),
    path('services/create/', service_create, name='service_create'),
    path('services/<int:pk>/update/', service_update, name='service_update'),
    path('services/<int:pk>/delete/', service_delete, name='service_delete'),
    path('advertising-campaigns/', advertising_campaign_list, name='advertising_campaign_list'),
    path('advertising-campaigns/create/', advertising_campaign_create, name='advertising_campaign_create'),
    path('advertising-campaigns/<int:pk>/update/', advertising_campaign_update, name='advertising_campaign_update'),
    path('advertising-campaigns/<int:pk>/delete/', advertising_campaign_delete, name='advertising_campaign_delete'),
    path('contracts/', contract_list, name='contract_list'),
    path('contracts/create/', contract_create, name='contract_create'),
    path('contracts/<int:pk>/', contract_detail, name='contract_detail'),
    path('contracts/<int:pk>/update/', contract_update, name='contract_update'),
    path('contracts/<int:pk>/delete/', contract_delete, name='contract_delete'),
]
