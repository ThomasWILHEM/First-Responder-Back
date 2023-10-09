from utils.db_seeder import DatabaseSeeder
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from .views import BuildingTypeList

# Create your tests here.


class BuildingTypeTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = BuildingTypeList.as_view()
        self.url = reverse('all-building-types')
        DatabaseSeeder().seed_database()

    def test_list_building_type(self):
        request = self.factory.get(self.url)
        response = self.view(request)

        data = [
            {
                "id": 1,
                "name": "Poste de police"
            },
            {
                "id": 2,
                "name": "Centre hospitalier"
            },
            {
                "id": 3,
                "name": "Caserne de pompier"
            }
        ]

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data, data)