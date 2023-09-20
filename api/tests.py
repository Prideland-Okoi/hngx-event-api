from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Event, Group
from django.contrib.auth.hashers import make_password

# Create your tests here.

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create a test user
        self.user = User.objects.create(
            username='testuser',
            password=make_password('testpassword')
            # Add other user fields as needed
        )

        # Create a test event
        self.event = Event.objects.create(
            title='Test Event',
            description='This is a test event.'
            # Add other event fields as needed
        )

        # Create a test group
        self.group = Group.objects.create(
            group_name='Test Group',
            description='This is a test group.',
            owner_id=self.user.id
        )

    # User Management Tests
    def test_user_registration(self):
        data = {
            'username': 'newuser',
            'password': 'newpassword'
            # Add other user fields as needed
        }
        response = self.client.post('/api/users/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_profile(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/users/profile/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Event Management Tests
    def test_create_event(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'New Event',
            'description': 'This is a new event.'
            # Add other event fields as needed
        }
        response = self.client.post('/api/events/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_event_detail(self):
        response = self.client.get(f'/api/events/{self.event.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # User Interactions Tests
    def test_add_user_to_group(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'userId': self.user.id
        }
        response = self.client.post(f'/api/groups/{self.group.id}/members/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_remove_user_from_group(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/api/groups/{self.group.id}/members/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

