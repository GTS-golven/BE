from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.get_token_url = '/api/auth/token'
        
        self.user_data = {
            'username': 'test',
            'password': 'tertadgdgsh13443',
            }
        
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()