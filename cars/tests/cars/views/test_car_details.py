from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from cars.web_cars.models import Car, Like

UserModel = get_user_model()


class CarDetailsTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email='test1@test.test', password='12345')
        self.user2 = UserModel.objects.create_user(email='test2@test2.test2', password='22222')

    def test_get_carDetails_when_carExistAndOwner_should_return_details(self):
        self.client.force_login(self.user)
        car = Car.objects.create(
            car_brand='Test Brand',
            car_model='Test Model',
            type='Test Type',
            engine='petrol',
            hp=1,
            transmission='auto',
            year=1,
            image='',
            mileage=1,
            user=self.user,
        )

        response = self.client.get(reverse('car details', kwargs={
            'pk': car.id,
        }))

        self.assertTrue(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])

    def test_carExistAndNotOwner_andNotLiked_should_return_details(self):
        self.client.force_login(self.user)
        car = Car.objects.create(
            car_brand='Test Brand',
            car_model='Test Model',
            type='Test Type',
            engine='petrol',
            hp=1,
            transmission='auto',
            year=1,
            image='',
            mileage=1,
            user=self.user2,
        )

        response = self.client.get(reverse('car details', kwargs={
            'pk': car.id,
        }))

        self.assertFalse(response.context['is_owner'])
        self.assertFalse(response.context['is_liked'])

    def test_carExistAndNotOwner_andLiked_should_return_details(self):
        self.client.force_login(self.user)
        car = Car.objects.create(
            car_brand='Test Brand',
            car_model='Test Model',
            type='Test Type',
            engine='petrol',
            hp=1,
            transmission='auto',
            year=1,
            image='',
            mileage=1,
            user=self.user2,
        )

        Like.objects.create(
            car=car,
            user=self.user,
        )

        response = self.client.get(reverse('car details', kwargs={
            'pk': car.id,
        }))

        self.assertFalse(response.context['is_owner'])
        self.assertTrue(response.context['is_liked'])

