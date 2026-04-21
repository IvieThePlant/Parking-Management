import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from .models import ParkingLot, ParkingSession


class ParkingSessionModelTests(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.user = get_user_model().objects.create_user(
			username='testuser',
			password='password123',
		)
		cls.lot = ParkingLot.objects.create(name='Lot A')

	def test_new_session_is_active(self):
		session = ParkingSession.objects.create(lot=self.lot, user=self.user)

		self.assertIsNone(session.ended_at)
		self.assertTrue(session.is_active)

	def test_end_session_sets_ended_at(self):
		session = ParkingSession.objects.create(lot=self.lot, user=self.user)

		session.end_session()

		self.assertIsNotNone(session.ended_at)
		self.assertFalse(session.is_active)

	def test_duration_for_ended_session(self):
		occupied_at = timezone.now() - datetime.timedelta(hours=3)
		ended_at = occupied_at + datetime.timedelta(hours=2, minutes=15)

		session = ParkingSession.objects.create(lot=self.lot, user=self.user)
		session.occupied_at = occupied_at
		session.ended_at = ended_at
		session.save(update_fields=['occupied_at', 'ended_at'])

		self.assertEqual(session.duration, datetime.timedelta(hours=2, minutes=15))
