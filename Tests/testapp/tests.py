from django.test import TestCase
from datetime import datetime
from .models import Happy

# Create your tests here.

class HappyModelTest(TestCase):

    @classmethod

    def setUpTestData(cls):
        cls.happy = Happy.object.create(
            first_name="Mike",
            last_name="Josh"
        )

    def test_fields(self):
        self.assertIsinstance(self.happy.first_name, str)
        self.assertIsInstance(self.happy.last_name, str)

    def test_timestamps(self):
        self.assertIsinstance(self.happy.booking_time, datatime)