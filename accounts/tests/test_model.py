from .test_setup import TestSetUp

from django.contrib.auth import get_user_model
User = get_user_model()

class TestModels(TestSetUp):
    def test_can_add_user(self):
        response = User.objects.create(
            username = self.user_data['username'],
            password = self.user_data['password']
        )
        
        self.assertEqual(response.username, self.user_data['username'])
        self.assertEqual(response.password, self.user_data['password'])
        
    def test_can_add_user_with_name(self):
        response = User.objects.create(
            username = self.user_data['username'],
            password = self.user_data['password'],
            first_name = self.user_first_and_last_name['first_name'],
            last_name = self.user_first_and_last_name['last_name'] 
        )
        
        self.assertEqual(response.username, self.user_data['username'])
        self.assertEqual(response.password, self.user_data['password'])
        self.assertEqual(response.first_name, self.user_first_and_last_name['first_name'])
        self.assertEqual(response.last_name, self.user_first_and_last_name['last_name'])