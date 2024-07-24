from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Car

# Create your tests here.
class CarModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username='testuser1',
            email='kSb3i@example.com',
            password='12345',
        )

        cls.testCar = Car.objects.create(
            model='testmodel',
            brand='testbrand',
            price=100,
            is_bought=False,
            buyer=testuser1,
            buy_time=None
        )

    def test_str_method(self):
        car = Car.objects.get(id=self.testCar.id)
        expected_object_name = f"{car.brand} {car.model} - ${car.price}"
        self.assertEqual(expected_object_name, str(car))
