from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker

import os, glob

from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files import File

from django.contrib.auth import get_user_model
User = get_user_model()

class TestSetUp(APITestCase):
    def setUp(self):
        self.user_create = reverse('user-create')
        self.get_token_url = '/api/auth/token'
        
        self.fake = Faker()
        
        self.user_data = {
            'username': self.fake.user_name(),
            'password': self.fake.password(),
            }
        
        self.user = User.objects.create(
            username = self.fake.user_name(),
            password = self.fake.password(),
        )

        self.user_updated_username = {
            'password': self.fake.user_name(),
        }
                
        self.user_updated_password = {
            'password': self.fake.password(),
        }
        
        self.user_first_and_last_name = {
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name()
        }
        
        self.file = SimpleUploadedFile(
            "test.jpg", 
            b"abc", 
            content_type="text/plain"
        )
        
        return super().setUp()
    
    def tearDown(self):
        
        for filename in glob.glob("media/accounts/test*"):
            os.remove(filename)
            
        for filename in glob.glob(f"media/accounts/{self.user.id}*"):
            os.remove(filename) 
            
        return super().tearDown()