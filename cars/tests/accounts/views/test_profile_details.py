from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from cars.accounts.models import Profile
from cars.web_cars.models import Car

UserModel = get_user_model()


class CarsTestCase(TestCase):
    def assertListEmpty(self, ll):
        return self.assertListEqual([], ll, 'The list is not empty!')


class ProfileDetailsTest(CarsTestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'test@test.test',
        'password': '12345',
    }

    VALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'User',
        'total_cars': 0,
        'profile_image': '',
    }

    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email='test1@test.test', password='12345')

    def test_when_logged_in_user_should_get_details_no_cars(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile details'))

        cars = list(response.context['cars'])
        profile = response.context['profile']

        self.assertListEmpty(cars)
        self.assertEqual(self.user.id, profile.user.id)

    def test_when_logged_in_user_should_get_details_with_cars(self):
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

        self.client.force_login(self.user)

        response = self.client.get(reverse('profile details'))

        profile = response.context['profile']

        self.assertEqual([car], list(response.context['cars']))
        self.assertEqual(self.user.id, profile.user.id)

    # def test_expect_correct_template(self):
    #     self.client.force_login(self.user)
    #     profile = Profile.objects.create(
    #         **self.VALID_PROFILE_DATA,
    #         user=self.user,
    #     )
    #
    #     response = self.client.get(reverse('profile details', kwargs={
    #         'pk': profile.id,
    #     }))
    #
    #     self.assertTemplateUsed('accounts/profile-details.html')

    # def test_when_userHasNoCars_expect_emptyList(self):
    #     profile = Profile.objects.create(
    #         **self.VALID_PROFILE_DATA,
    #         user=self.user,
    #     )
    #
    #     response = self.client.get(reverse('profile details', kwargs={
    #         'pk': profile.pk+1
    #     }))
    #
    #     self.assertEqual(
    #         [],
    #         response.context['cars'],
    #     )