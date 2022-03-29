from django.urls import reverse
from rest_framework.test import force_authenticate

from .test_setup import TestSetUp

class TestViews(TestSetUp):
    def test_cannot_register_without_data(self):
        response = self.client.post(self.user_create)
        
        self.assertEqual(response.status_code, 400)
                
    def test_can_register_with_username_password(self):
        response = self.client.post(
            self.user_create, self.user_data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_can_register_with_username_password_name(self):
        data = {**self.user_data, **self.user_first_and_last_name }
        response = self.client.post(
            self.user_create, data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_can_change_username(self):
        request = self.factory.patch(
            reverse('user-edit', args=[self.user.id]),
            self.user_updated_username
        )
        
        force_authenticate(request, user=self.user)
            
        response = self.view(request, pk=self.user.id)
       
        self.assertEqual(response.status_code, 200)
        
    def test_can_change_password(self):
        request = self.factory.patch(
            reverse('user-edit', args=[self.user.id]),
            self.user_updated_password
        )
        
        force_authenticate(request, user=self.user)
            
        response = self.view(request, pk=self.user.id)
        
        self.assertEqual(response.status_code, 200)
        
    def test_can_set_first_and_last_name(self):
        request = self.factory.patch(
            reverse('user-edit', args=[self.user.id]),
            self.user_first_and_last_name
        )
        
        force_authenticate(request, user=self.user)
            
        response = self.view(request, pk=self.user.id)
        
        self.assertEqual(response.status_code, 200)
        
    def test_can_delete(self):
        request = self.factory.delete(
            reverse('user-edit', args=[self.user.id])
        )
        
        force_authenticate(request, user=self.user)
            
        response = self.view(request, pk=self.user.id)
        
        self.assertEqual(response.status_code, 204)
        
    def test_can_upload_picture(self):
        payload = {
            'profile_pic': self.file
        }
        
        request = self.factory.patch(
            reverse('user-edit', args=[self.user.id]),
            payload,
        )
        
        force_authenticate(request, user=self.user)
            
        response = self.view(request, pk=self.user.id)
        
        self.assertEqual(response.status_code, 200)