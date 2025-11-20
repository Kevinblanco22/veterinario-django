import datetime
from django.test import TestCase
from django.urls import reverse
from .models import Owner, Pet


class PetDetailViewTests(TestCase):
    def test_pet_detail_returns_404_for_nonexistent_pet(self):
        url = reverse('clinic:pet_detail', args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class PetModelTests(TestCase):
    def test_str_returns_name_and_species(self):
        owner = Owner.objects.create(
            name="Juan",
            phone="123",
            email="juan@example.com"
        )
        pet = Pet.objects.create(
            owner=owner,
            name="Firulais",
            species="Perro",
            birth_date=datetime.date(2020, 1, 1)
        )
        self.assertEqual(str(pet), "Firulais (Perro)")
