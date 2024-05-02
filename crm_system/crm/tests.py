# crm/tests.py

from django.test import TestCase
from .models import Service


class ServiceModelTest(TestCase):
    def test_service_creation(self):
        service = Service.objects.create(name="Test Service", description="Test Description", cost=100.00)
        self.assertEqual(service.name, "Test Service")
        self.assertEqual(service.cost, 100.00)
